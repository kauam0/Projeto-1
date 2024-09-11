from django.urls import path
from Loja_app import views

urlpatterns = [
    path('', views.cadastro, name='home'),
    # rota para as informaçoes do usuario
    path('registro/', views.usuarios, name='listagem_usuarios'),
    
    path('login/', views.login, name='login')
 
]