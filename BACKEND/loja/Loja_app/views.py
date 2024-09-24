from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render
from .models import Usuario
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import  RegistroForm, LoginForm



def loginn (request):
    form = LoginForm(request.POST or None)
    context = {
                    "form": form
              }
    print("User logged in")
    #print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password) 
        print(user)
        #print(request.user.is_authenticated)
        if user is not None:
            #print(request.user.is_authenticated)
            login(request, user)
            print("Login válido")
            # Redireciona para uma página de sucesso.
            return redirect("/")
        else:
            #Retorna uma mensagem de erro de 'invalid login'.
            print("Login inválido")
    return render(request, "auth/login.html", context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
                    "form": form
              }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render (request, 'usuarios/regL/login.html')

def registro (request):
    return render (request, 'usuarios/regL/registro.html')

def home(request):
      if request.user.is_authenticated:
        context["premium_content"] = "Você é um usuário Premium"
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
    

  