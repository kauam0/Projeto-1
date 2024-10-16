from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginn, name='login'),
    
    path('registro/', views.registro, name='registro'),

    path('carrinho/', views.carrinho,  name='carrinho')

    
    ]