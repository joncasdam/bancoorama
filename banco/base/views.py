# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
# from django.http import JsonResponse

from contas.models import Transacao

from base.models import Perfil

def index(request):
    return render(request, "index.html")

@login_required(login_url='/')
def dashboard(request):
    contexto = {}
    conta = request.user.perfil.conta
    contexto['saldo_atual']= conta.saldo_conta
    if request.is_ajax():
        return render(request, 'dashboard_ajax.html', contexto)
    else:
        return render(request, 'dashboard.html', contexto)

@login_required(login_url='/')
def extrato(request):
    contexto = {}
    conta = request.user.perfil.conta
    contexto['extrato'] = [i.to_dict() for i in conta.transacoes.all()]
    return render(request, 'extrato.html', contexto)

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
