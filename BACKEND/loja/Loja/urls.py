from django.urls import path
from Loja_app import views

urlpatterns = [
    path('', views.cadastro, name='home'),
    # rota para as informaçoes do usuario
    path('informacao/', views.usuarios, name='listagem_usuarios'),
    
    path('login/', views.loginn, name='login'),
    
    path('registro/', views.registro, name='registro')
 
]