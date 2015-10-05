# -*- encoding: utf-8 -*-
from random import randint

from djmoney.models.fields import MoneyField
from django.db import models

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