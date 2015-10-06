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
    correntista = models.OneToOneField(Perfil, verbose_name=u'Correntista', related_name='conta')
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

    @property
    def saldo_int(self):
        return int(self.saldo.amount)

    def ultima_transacao(self, tipo=None):
        try:
            if tipo == Transacao.SAQUE:
                ultima = self.transacoes.filter(tipo=Transacao.SAQUE).latest('id')
            elif tipo == Transacao.DEPOSITO:
                ultima = self.transacoes.filter(tipo=Transacao.DEPOSITO).latest('id')
            else:
                ultima = self.transacoes.latest('id')
            return u'{}'.format(ultima.data_e_valor)
        except:
            return u'Ainda sem registro'

    @property
    def ultimo_item_extrato(self):
        return self.ultima_transacao()

    @property
    def ultimo_deposito(self):
        return self.ultima_transacao(Transacao.DEPOSITO)

    @property
    def ultimo_saque(self):
        return self.ultima_transacao(Transacao.SAQUE)

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
        ordering = ['-data_criacao',]

    def __unicode__(self):
        return u'{} de {}'.format(self.TIPOS[self.tipo-1][1], self.valor)


    @staticmethod
    def valor_formatado(valor):
        return '{}'.format(format_money(valor, locale=settings.LANGUAGE_CODE))

    @property
    def data_e_valor(self):
        data = '{:%d-%m-%Y, %H:%M}'.format(self.data_criacao)
        return '{} - {}'.format(data, self.valor_formatado(self.valor))

    @classmethod
    def faz_transacao(cls, conta, valor, tipo):
        valor_formatado = Money(valor, BRL)
        if tipo == cls.SAQUE:
            novo_saldo = conta.saldo - valor_formatado
        else:
            novo_saldo = conta.saldo + valor_formatado
        try:
            cls.objects.create(conta=conta, valor=valor_formatado, tipo=tipo, saldo=novo_saldo)
            conta.saldo = novo_saldo
            conta.save()
            return True
        except:
            return False

    @classmethod
    def faz_deposito(cls, conta, valor):
        return cls.faz_transacao(conta, valor, cls.DEPOSITO)

    @classmethod
    def faz_saque(cls, conta, valor):
        return cls.faz_transacao(conta, valor, cls.SAQUE)

    def to_dict(self):
        return {'id': self.id,
                'valor': self.valor_formatado(self.valor),
                'data': '{:%d-%m-%Y %H:%M}'.format(self.data_criacao),
                'tipo': self.tipo,
                'tipo_str': self.TIPOS[self.tipo-1][1],
                'saldo': self.valor_formatado(self.saldo)}
