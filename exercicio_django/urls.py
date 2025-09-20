"""
URL configuration for exercicio_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='cadastro'),
    path('login/', views.login, name='login'),
    path('home/', views.usuarios, name='homepage'),
    path('logout/', views.fazer_logout, name='logout'),
    path('adicionar_produto/', views.adicionar_produto, name='adicionar_produto'),
    path('remover_produto/<int:produto_id/', views.remover_produto, name='remover_produto'),
]
