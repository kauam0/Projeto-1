from django.urls import path
from Loja_app import views

urlpatterns = [
    path('', views.home, name='home'),
    # rota para as informaçoes do usuario
    path('registro/', views.usuarios, name='listagem_usuarios'),
    path('registro/local/', views.localizacao, name='local'),
]