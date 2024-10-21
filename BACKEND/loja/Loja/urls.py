from django.urls import path, include
from Loja_app import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # rota para as informaçoes do usuario
    path('informacao/', views.usuarios, name='listagem_usuarios'),
    path('produtos/', include("produtos.urls"))
    path('auth/', include("Loja_app.urls"))
 
]