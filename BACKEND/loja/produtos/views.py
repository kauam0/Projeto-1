from django.shortcuts import render, redirect
from .form import dadosProduto, imagemProduto
from django.http import HttpResponse
from .models import Produtos

def  criar_produto(request):
  
    if request.method == 'POST':
        form_produto = dadosProduto(request.POST)
        form_imagem = imagemProduto(request.POST, request.FILES)
        if form_produto.is_valid() and form_imagem.is_valid():
            produto = form_produto.save()
            imagem = form_imagem.save()
            imagem.produto = produto
            imagem.save()
            return HttpResponse ('Produto criado com sucesso!')
        else:
            return render(request,'usuarios/formProduto.html', {'form_produto': form_produto, 'form_imagem': form_imagem})
    else:
        form_produto = dadosProduto()
        form_imagem = imagemProduto()

    return render(request, 'usuarios/formProduto.html', {
        'form_produto': form_produto,
        'form_imagem': form_imagem,
    })

def lista_produto(request):
    produtos = Produtos.objects.all()
    return render(request,'usuarios/home.html', {'produtos': produtos})
    

