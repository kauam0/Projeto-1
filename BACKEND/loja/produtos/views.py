from django.shortcuts import render, redirect
from .form import dadosProduto, imagemProduto
from .models import Produtos, ImagemProdutos

def  criar_produto(request):
    if request.method == 'Post':
        form_produto = dadosProduto(request.POST)
        form_imagem = imagemProduto(request.POST, request.FILES)
        if form_produto.is_valid() and form_imagem.is_valid():
            produto = form_produto.save()
            imagem = form_imagem(comit=False)
            imagem.produto = produto
            imagem.save()
            return redirect('sucesso')
        else:
            form_produto = dadosProduto()
            form_imagem = imagemProduto

        return render(request, 'formProduto.html', {'form_produto':form_produto, 'form_imagem':form_imagem})


