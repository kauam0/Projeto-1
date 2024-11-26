from django.urls import path, include
from django.contrib.auth import views as auth_views
from Loja_app import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('informacao/', views.usuarios, name='listagem_usuarios'),

    path('usuarios/', include('Loja_app.urls')),
    path('auth/', include("Loja_app.urls")),
    path('logout/', auth_views.LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('produtos/', include("produtos.urls")),
    path('auth/', include("Loja_app.urls")),
 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

