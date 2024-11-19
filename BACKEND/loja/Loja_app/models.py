from django.db import models
from django.contrib.auth.hashers import make_password

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nascimento = models.DateField(null=True, blank=True)
    telefone = models.IntegerField()
    cep = models.CharField(max_length=10)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    rua = models.CharField(max_length=100, null=True, blank=True)
    numero_casa = models.IntegerField()
    complemento = models.CharField(max_length=255, blank=True, null=True)
    

    
