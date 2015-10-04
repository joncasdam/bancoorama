# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    CORRENTISTA = 1
    ADMINISTRADOR = 2

    TIPOS = (
        (CORRENTISTA, u'Correntista'),
        (ADMINISTRADOR, u'Administrador'),
    )
    user = models.ForeignKey(User, related_name='perfil', verbose_name=u'Usuário')
    tipo = models.IntegerField(u'Tipo', choices=TIPOS, default=CORRENTISTA, blank=True, null=True)

    class Meta:
        verbose_name = u'Perfil'
        verbose_name_plural = u'Perfis'

    def __unicode__(self):
        return u'%s' % self.user

    @property
    def eh_correntista(self):
        return True if self.tipo == self.CORRENTISTA else False

    @property
    def eh_administrador(self):
        return True if self.tipo == self.ADMINISTRADOR else False


class Banco(models.Model):
    nome = models.CharField(u'Nome', max_length=250, null=False, blank=False, unique=True)

    class Meta:
        verbose_name = u'Banco'
        verbose_name_plural = u'Bancos'

    def __unicode__(self):
        return u'%s' % self.nome