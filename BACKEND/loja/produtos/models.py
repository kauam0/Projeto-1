from django.db import models

# Create your models here.

class Produtos(models.Model):
    id_produtos = models.AutoField(primary_key=True)
    nome_produtos = models.CharField(max_length= 140)
    preco_produtos = models.DecimalField(max_digits=10, decimal_places=2)
    img_produtos = models.ImageField(upload_to="cars")
    descricao_produtos = models.CharField(max_length=255)
    quantidade_de_variacao = models.IntegerField()
    categoria_produtos = models.CharField(max_length= 140)
    data_de_iniciacao = models.DateTimeField.auto_now_add()
