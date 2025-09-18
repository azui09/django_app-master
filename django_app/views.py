from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login

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
            messages.success(request, f"Bem vindo de volta, {username}!")
            return redirect('homepage')
        else:
            messages.error(request, f"Usuário ou senha inválidos, tente novamente!")
            return redirect("login")
    else:
        return render(request, "usuarios/login.html")


def usuarios(request):
    return render(request, "usuarios/homepage.html")