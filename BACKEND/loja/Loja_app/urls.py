from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginn, name='loginn'),
    
    path('registro/', views.registro, name='listagem_usuarios')]