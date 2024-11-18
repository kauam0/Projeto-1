from django.db import models

# Create your models her
class Produtos(models.Model):
    id_produtos = models.AutoField(primary_key=True)
    nome_produtos = models.CharField(max_length=140)
    preco_produtos = models.DecimalField(max_digits=10, decimal_places=2)
    descricao_produtos = models.CharField(max_length=255)
    quantidade_de_variacao = models.IntegerField()
    categoria_produtos = models.CharField(max_length=140)
    data_de_iniciacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_produtos

class ImagemProdutos(models.Model):
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE, null=True)
    imagem = models.ImageField(upload_to='media')

    def __str__(self):
        return f"Imagem de {self.produto.nome_produtos}"