from django.shortcuts import render
from .models import Usuario, Localizacao

def home(request):
    # formulario
    return render(request,'usuarios/home.html')

def usuarios(request):
    #salvar
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.nascimento = request.POST.get('telefone')
    novo_usuario.telefone = request.POST.get('email')
    novo_usuario.senha = request.POST.get('senha')
    novo_usuario.save()

    usuarios = {
        'usuarios' : Usuario.objects.all()
    }
    return render(request,'usuarios/usuarios.html', usuarios)

def localizacao(request):
    #salvar localiçao
    novo_localizacao = Localizacao()
    novo_localizacao.cep = request.POST.get('cep')
    novo_localizacao.locradouro = request.POST.get('bairro')
    novo_localizacao.rua = request.POST.get('rua')
    novo_localizacao.complemento = request.POST.get('complemento')
    novo_localizacao.save()

    localizacao = {
        'localizacoes' : Localizacao.objects.all()
    }
    return render(request,'usuarios/usuarios.html', localizacao)

class IndexView(TemplateView):
    template_name = "index.html"
