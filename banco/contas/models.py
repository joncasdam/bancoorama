# -*- encoding: utf-8 -*-
from random import randint
from moneyed.classes import Money
from moneyed import BRL
from moneyed.localization import format_money

from djmoney.models.fields import MoneyField
from django.db import models
from django.conf import settings

from utils.models import BaseModel, BaseManager
from base.models import Perfil, Banco


class Agencia(models.Model):
    banco = models.ForeignKey(Banco, verbose_name=u'Banco', related_name='agencias')
    codigo = models.IntegerField(u'Código', editable=False, unique=True)

    objects = BaseManager()

    class Meta:
        verbose_name = u'Agência'
        verbose_name_plural = u'Agências'

    def __unicode__(self):
        return '%s' % self.codigo

    @staticmethod
    def gera_numero_agencia():
        numero = randint(0, (10 ** 4) - 1)
        return '{:04}'.format(numero, 4)

    def save(self, *args, **kwargs):
        if not self.codigo:
            codigo = self.gera_numero_agencia()
            while Agencia.objects.get_or_none(codigo=codigo):
                codigo = self.gera_numero_agencia()
            self.codigo = codigo
        super(Agencia, self).save(*args, **kwargs)



class Conta(BaseModel):
    agencia = models.ForeignKey(Agencia, verbose_name=u'Agência', related_name='contas')
    numero = models.IntegerField(u'Número', editable=False, unique=True)
    correntista = models.ForeignKey(Perfil, verbose_name=u'Correntista', related_name='conta')
    saldo = MoneyField(max_digits=10, decimal_places=2, default_currency='BRL')

    class Meta:
        verbose_name = u'Conta'
        verbose_name_plural = u'Contas'

    def __unicode__(self):
        return u'{} {} {}'.format(self.agencia, self.numero, self.correntista)

    @staticmethod
    def gera_numero_conta():
        numero = randint(0, (10 ** 5) - 1)
        return '{:05}'.format(numero, 5)

    def save(self, *args, **kwargs):
        if not self.id and Conta.objects.get_or_none(correntista=self.correntista):
            return
        if not self.numero:
            numero = self.gera_numero_conta()
            while Conta.objects.get_or_none(numero=numero):
                numero = self.gera_numero_conta()
            self.numero = numero
        super(Conta, self).save(*args, **kwargs)

    @property
    def saldo_conta(self):
        return format_money(self.saldo, locale=settings.LANGUAGE_CODE)

    @classmethod
    def cria_conta(cls, correntista):
        cls.objects.create(agencia_id=1, correntista=correntista)


class Transacao(BaseModel):
    SAQUE = 1
    DEPOSITO = 2

    TIPOS = (
        (SAQUE, 'Saque'),
        (DEPOSITO, u'Depósito'),
    )

    conta = models.ForeignKey(Conta, verbose_name=u'Conta', related_name='transacoes')
    valor = MoneyField(u'Valor', max_digits=10, decimal_places=2, default_currency='BRL')
    tipo = models.IntegerField(u'Tipo', choices=TIPOS, default=SAQUE, blank=True, null=True)
    saldo = MoneyField(u'Saldo', max_digits=10, decimal_places=2, default_currency='BRL')

    class Meta:
        verbose_name = u'Transação'
        verbose_name_plural = u'Transações'

    def __unicode__(self):
        return '{} de {} feito por {} '.format(self.TIPOS[self.tipo][1], self.valor, self.conta)

    @classmethod
    def faz_saque(cls, conta, valor):
        novo_saldo = Money(conta.saldo, BRL) - Money(valor, BRL)
        try:
            cls.objects.create(conta=conta, valor=valor, tipo=cls.SAQUE, saldo=novo_saldo)
            conta.saldo = novo_saldo
            conta.save()
            return True
        except:
            return False

    @classmethod
    def faz_deposito(cls, conta, valor):
        novo_saldo = Money(conta.saldo, BRL) + Money(valor, BRL)
        try:
            cls.objects.create(conta=conta, valor=valor, tipo=cls.DEPOSITO, saldo=novo_saldo)
            conta.saldo = novo_saldo
            conta.save()
            return True
        except:
            return False
