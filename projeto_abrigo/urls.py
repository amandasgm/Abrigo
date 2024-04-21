"""
URL configuration for projeto_abrigo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_geral.views import inicio, sugestão, sucesso
from app_usuarios.views import usuario
from app_animais.views import gatos, perros
from app_voluntarios.views import voluntarios
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='iniciar'),
    path('usuarios/', usuario, name='usuarios'),
    path('voluntarios/', voluntarios, name='voluntarios'),
    path('gatos/', gatos, name='gatos'),
    path('perros/', perros, name='cachorros'),
    path('sugestão/', sugestão, name='sugestão'),
    path('sucesso/', sucesso, name='sucesso')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )+ [
    # Definindo o caminho para servir arquivos estáticos durante o desenvolvimento
    # Isso serve arquivos estáticos em STATIC_URL (ex: '/static/') para STATIC_ROOT (ex: 'static/')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


