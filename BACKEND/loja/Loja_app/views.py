from django.shortcuts import render
from .models import Usuario
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


def loginn (request):
    return render (request, 'usuarios/regL/login.html')

def registro (request):
    return render (request, 'usuarios/regL/registro.html')

def cadastro(request):
    return render(request, 'usuarios/home.html')
 
 

def usuarios(request):
    #salvar
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.nascimento = request.POST.get('nascimento')
    novo_usuario.telefone = request.POST.get('telefone')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.senha = request.POST.get('senha')
    novo_usuario.cep = request.POST.get('cep')
    novo_usuario.bairro = request.POST.get('bairro')
    novo_usuario.numero_casa = request.POST.get('numero_casa')
    novo_usuario.rua = request.POST.get('rua')
    novo_usuario.complemento = request.POST.get('complemento')
    novo_usuario.save()
   
    usuarios = {
        'usuarios' : Usuario.objects.all()
    }
    
    return render(request,'usuarios/home.html',usuarios)
    
    

     
   

    #salvar localiçao
    

  