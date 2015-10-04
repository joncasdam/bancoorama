# -*- encoding: utf-8 -*-
from djmoney.models.fields import MoneyField
from django.db import models

from utils.models import BaseModel
from base.models import Perfil, Banco


class Agencia(models.Model):
    banco = models.ForeignKey(Banco, verbose_name=u'Banco', related_name='agencias')
    codigo = models.IntegerField(u'Código', editable=False, unique=True)

    class Meta:
        verbose_name = u'Agência'
        verbose_name_plural = u'Agências'

    def __unicode__(self):
        return '%s' % self.codigo


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