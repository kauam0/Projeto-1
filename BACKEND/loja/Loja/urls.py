from django.urls import path, include
from Loja_app import views
from django.contrib import admin

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # rota para as informaçoes do usuario
   
    path('auth/', include("Loja_app.urls")),
    path('acconts/', include('django.contrib.auth.urls')),
    
 
]
