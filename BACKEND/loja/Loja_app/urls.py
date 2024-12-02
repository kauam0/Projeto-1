from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('login/', views.loginn, name='loginn'),
    
    path('carrinho/', views.carrinho,  name='carrinho'),

    path('registro/', views.registro, name='listagem_usuarios'),

    path('tela_de_usuario/' , views.tela_de_usuario, name='tela_de_usuario'),

    path('registro/', views.registro, name='listagem_usuarios'),
    
   

    path('tela_edit/', views.tela_edit, name='tela_edit' )
    ]


