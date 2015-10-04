# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    CORRENTISTA = 0
    ADMINISTRADOR = 1

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
