# -*- encoding: utf-8 -*-
from decimal import Decimal

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

from contas.models import Conta, Transacao

from base.models import Perfil

def index(request):
    return render(request, "index.html")

@login_required(login_url='/')
def dashboard(request):
    contexto = {}
    conta = request.user.perfil.conta
    contexto['saldo_atual']= conta.saldo_conta
    contexto['ultima_transacao'] = conta.ultimo_item_extrato
    contexto['ultimo_deposito'] = conta.ultimo_deposito
    contexto['ultimo_saque'] = conta.ultimo_saque

    if request.user.is_staff:
        contexto['total_sacado'] = Transacao.total_por_tipo(Transacao.SAQUE)
        contexto['total_depositado'] = Transacao.total_por_tipo(Transacao.DEPOSITO)
        contexto['total_em_caixa'] = Conta.total_em_caixa()
    if request.is_ajax():
        return render(request, 'dashboard_ajax.html', contexto)
    else:
        return render(request, 'dashboard.html', contexto)

@csrf_exempt
@login_required(login_url='/')
def saque(request):
    contexo = {}
    conta = request.user.perfil.conta
    if request.method == 'POST':
        valor = request.body.split('=')[1]
        # nao eh o melhor lugar mas fica aqui por hora
        if Decimal(valor) > conta.saldo.amount:
            contexo['error'] = 'Saldo insuficiente'
        else:
            try:
                sacando = Transacao.faz_saque(conta, valor)
                if sacando:
                    contexo['sucesso'] = True
            except:
                contexo['error'] = u'Houve um erro na requisição'

    contexo.update({'saldo_atual': conta.saldo,
                    'saldo_int': conta.saldo_int})
    return render(request, 'saque.html', contexo)

@csrf_exempt
@login_required(login_url='/')
def deposito(request):
    contexto = {}
    conta = request.user.perfil.conta
    if request.method == 'POST':
        valor = request.body.split('=')[1]
        try:
            depositando = Transacao.faz_deposito(conta, valor)
            if depositando:
                contexto['sucesso'] = True
        except:
            contexto['error'] = True
    contexto.update({'saldo_atual': conta.saldo,})
    return render(request, 'deposito.html', contexto)

@login_required(login_url='/')
def extrato(request):
    contexto = {}
    if request.user.is_staff:
        tipo = request.GET.get('tipo', None)
        contexto['extrato'] = Transacao.todas_do_dia(tipo=tipo)
    else:
        conta = request.user.perfil.conta
        contexto['extrato'] = [i.to_dict() for i in conta.transacoes.all()]
    return render(request, 'extrato.html', contexto)

@login_required(login_url='/')
@staff_member_required
def listasaldos(request):
    contexto = {'extrato': [{'numero_conta': i.numero, 'saldo': i.saldo_conta} for i in
                            Conta.objects.all()]}
    return render(request, 'saldo_clientes.html', contexto)

def login_usr(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)
        senha = request.POST.get('senha', None)
        autentica = authenticate(username=email, password=senha)
        if autentica:
            try:
                login(request, autentica)
                return redirect('dashboard')
            except:
                pass
    return render(request, 'login.html')

def logout_usr(request):
    logout(request)
    return redirect('index')

def signup_usr(request):
    contexto = {}
    if request.method == 'POST':
        email = request.POST.get('email', None)
        senha = request.POST.get('senha', None)
        if all([email, senha]):
            if not Perfil.objects.get_or_none(user__email=email):
                perfil = Perfil.criar_correntista(request, email, senha)
                if perfil:
                    return redirect('dashboard')
                else:
                    contexto['error'] = 'Erro na criação de usuário'
            else:
                contexto['error'] = 'Já existe uma conta com esse e-mail'
        else:
            contexto['error'] = 'Preencha corretamente os dados'
    return render(request, 'signup.html', contexto)
