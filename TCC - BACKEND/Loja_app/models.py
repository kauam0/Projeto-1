from django.db import models




class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    nascimento = models.DateField()
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    senha = models.TextField(max_length=255)

class Localizacao(models.Model):
    id_localizacao = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cep = models.CharField(max_length=10)
    bairro = models.TextField(max_length=255)
    rua = models.TextField(max_length=255)
    locradouro = models.IntegerField()
    complemento = models.TextField(max_length=255)