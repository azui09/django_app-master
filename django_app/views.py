from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required

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
    dados_usuario = {
        'nome_usuario': request.user.username,
        'email_usuario': request.user.email,
        'id_usuario': request.user.id
    }

    return render(request, "usuarios/homepage.html", dados_usuario)

def fazer_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return redirect('login')