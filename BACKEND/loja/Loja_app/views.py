from django.shortcuts import render
from .models import Usuario
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


def loginn (request):
    if request.method == 'GET':
        return render (request, 'usuarios/regL/login.html')
    else:
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        user =  authenticate( email=email, password=senha)
        
        if user:#verificando se o usuario é valido
            login(request, user)
            return HttpResponse('Login realizado com sucesso')
        else:
           return HttpResponse("email ou senha invalidas")


def registro (request):
    if request.method == "GET":
        return render (request, 'usuarios/regL/registro.html')
    else:
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        
        user = User.objects.filter(email=email).first()
        if user:
            return HttpResponse('esse email ja existe')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        return HttpResponse('usuario cadastrado com sucesso')

def home(request):
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

   
     
   

    #salvar localiçao
    

  