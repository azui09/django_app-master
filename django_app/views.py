from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    if request.method == 'GET':
        return render(request, "usuarios/home.html")
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.get(username=username)

        if User.objects.filter(username=username).exists():
            return HttpResponse('Já existe um usuário com esse nome. Por favor, escolha outro.')
        else:
            return HttpResponse(f'Usuário {username} pode ser criado!')

        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return redirect("usuarios/login.html")

def login(request):
    return render(request, 'usuarios/login.html')

def usuarios(request):
    pass