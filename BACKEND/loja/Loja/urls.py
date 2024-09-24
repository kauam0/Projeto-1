from django.urls import path, include
from Loja_app import views

urlpatterns = [
    path('', views.home, name='home'),
    # rota para as informaçoes do usuario
    path('informacao/', views.usuarios, name='listagem_usuarios'),
    
    path('auth/', include("Loja_app.urls"))
 
]