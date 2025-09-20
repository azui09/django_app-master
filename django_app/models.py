from django.db import models
from django.contrib.auth.models import User

class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    email = models.EmailField()

class Produto(models.Model):
    nome_produto = models.CharField(max_length=255)
    qtd_produto = models.IntegerField()

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

