from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from .forms import ProdutoForm
from .models import Produto

def home(request):
    if request.method == 'GET':
        return render(request, "usuarios/home.html")
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if senha != confirmar_senha:
            messages.error(request, 'As senhas não coincidem!')
            return redirect('cadastro')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Este nome de usuário já está em uso!')
            return redirect('cadastro')

        user = User.objects.create_user(username=username, email=email, password=senha)
        
        return redirect('login')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)
        if user is not None:
            auth_login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, f"Usuário ou senha inválidos, tente novamente!")
            return redirect("login")
    else:
        return render(request, "usuarios/login.html")

@login_required(login_url='login')
def usuarios(request):
    produtos_do_usuario = Produto.objects.filter(usuario=request.user)
    contexto = {
        'produtos': produtos_do_usuario
    }

    return render(request, "usuarios/homepage.html", produtos_do_usuario)

def fazer_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return redirect('login')

@login_required(login_url='login')
def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.usuario = request.user
            produto.save()
            return redirect('homepage')
    else:
        form = ProdutoForm()
    return render(request, 'usuarios/adicionar_produto.html', {'form': form})

@login_required(login_url='login')
def remover_produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    if produto.usuario == request.user:
        produto.delete()
    return redirect('homepage')
        