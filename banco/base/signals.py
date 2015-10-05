# -*- encoding: utf-8 -*-
from contas.models import Conta

def perfil_post_save(sender, **kwargs):
    perfil = kwargs['instance']
    Conta.cria_conta(perfil)