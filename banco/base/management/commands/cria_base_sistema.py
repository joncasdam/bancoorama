# -*- encoding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from base.models import Perfil, Banco
from contas.models import Agencia, Conta

class Command(BaseCommand):
    '''
    Cria items básicos para sistema rodar
    '''
    args = ''
    help = u'Cria items básicos para sistema rodar'

    def handle(self, *args, **options):
        print 'Inicia rotina'
        # pega usuario admin criado
        admin = User.objects.get(id=1)
        admin.is_active = True
        admin.save()

        # cria um banco
        novo_banco = Banco.objects.create(nome='Banco Orama')
        # cria uma agencia no banco
        Agencia.objects.create(banco=novo_banco)
        # cria perfil para usuario admin
        # essa etapa já cria uma conta na agenca
        Perfil.objects.create(user=admin)

        print 'Rotina encerrada'