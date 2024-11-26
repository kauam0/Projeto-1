from django.urls import path
from . import views

urlpatterns = [
    path('', views.criar_produto, name='criar_produto')
    path('lista_produto', views.lista_produto, name='lista_produto'),
]