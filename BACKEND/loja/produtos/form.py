from django import forms
from .models import Produtos, ImagemProdutos

class dadosProduto(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = ['nome_produtos', 'preco_produtos', 'descricao_produtos', 'quantidade_de_variacao', 'categoria_produtos']
    
class imagemProduto(forms.ModelForm):
    class Meta:
        model = ImagemProdutos
        fields = ['imagem']