from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import EmailAuthenticationForm

def home(request):
    return render(request, 'usuarios/home.html')
 
def loginn(request):
    return render(request, 'usuarios/regL/login.html')

def loginn (request):
    if request.method == 'GET':
        form = EmailAuthenticationForm()
        return render(request, 'usuarios/regL/login.html', {'form': form})
    else:
        form = EmailAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['senha']
            user = authenticate(email=email, password=password)
            if user:
                login_django(request, user)
                return redirect('home')
            
            else:
                return render(request, 'usuarios/regL/login.html', {'form': form, 'error': 'E-mail ou senha incorretos'})
        else:
            return HttpResponse('error AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')  # Retorna o formulário com erros
       


def registro (request):
    if request.method == "GET":
        return render (request, 'usuarios/regL/registro.html')
    else:
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        
        
        user = User.objects.filter(email=email).first()
        user.set_password(senha)
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


    usuarios = {
        'usuarios' : Usuario.objects.all()
    }
    
    return render(request,'usuarios/home.html',usuarios)
    
    



   
     
   

    #salvar localiçao
    

  
  