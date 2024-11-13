from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginn, name='loginn'),
    
<<<<<<< HEAD
    path('registro/', views.registro, name='registro'),

    path('carrinho/', views.carrinho,  name='carrinho')

    
=======
    path('registro/', views.registro, name='listagem_usuarios'),
    
    

>>>>>>> backend
    ]