from django.db import models
from django.contrib.auth.hashers import make_password

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    nascimento = models.DateField()
    telefone = models.IntegerField()
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    cep = models.CharField(max_length=10)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=255)
    rua = models.CharField(max_length=255)
    numero_casa = models.IntegerField()
    complemento = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.senha = make_password(self.senha)
        super().save(*args, **kwargs)

class Produtos(models.Model):
    id_produtos = models.AutoField(primary_key=True)
    nome_do_produto = models.CharField(max_length=100)
    categoria = models.CharField(max_length=120)
    condicao = models.CharField(max_length=50)
    valor = models.FloatField()

