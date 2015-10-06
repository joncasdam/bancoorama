# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from signals import perfil_post_save
from utils.models import BaseManager


class Perfil(models.Model):
    CORRENTISTA = 1
    ADMINISTRADOR = 2

    TIPOS = (
        (CORRENTISTA, u'Correntista'),
        (ADMINISTRADOR, u'Administrador'),
    )
    user = models.OneToOneField(User, related_name='perfil', verbose_name=u'Usuário')
    tipo = models.IntegerField(u'Tipo', choices=TIPOS, default=CORRENTISTA, blank=True, null=True)

    objects = BaseManager()

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

    @classmethod
    def criar_correntista(cls, request, email, senha):
        usr = User.objects.create_user(email, email, senha)
        if usr:
            usr.is_active = True
            usr.save()
            try:
                authenticate(username=email, password=senha)
            except:
                return False
            novo_usuario = cls.objects.create(user=usr)
            if novo_usuario:
                from contas.models import Conta
                Conta.cria_conta(novo_usuario)
            return novo_usuario
        return False

models.signals.post_delete.connect(perfil_post_save, sender=Perfil)


class Banco(models.Model):
    nome = models.CharField(u'Nome', max_length=250, null=False, blank=False, unique=True)

    class Meta:
        verbose_name = u'Banco'
        verbose_name_plural = u'Bancos'

    def __unicode__(self):
        return u'%s' % self.nome