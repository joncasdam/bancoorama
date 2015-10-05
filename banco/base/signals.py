# -*- encoding: utf-8 -*-

def perfil_post_save(sender, **kwargs):
    from contas.models import Conta
    perfil = kwargs['instance']
    Conta.cria_conta(perfil)