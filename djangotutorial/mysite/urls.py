"""
Configuración de URLs para el proyecto mysite.

La lista `urlpatterns` enruta URLs a vistas. Para más información, por favor visita:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Ejemplos:
Vistas basadas en funciones
    1. Añadir una importación:  from my_app import views
    2. Añadir una URL a urlpatterns:  path('', views.home, name='home')
Vistas basadas en clases
    1. Añadir una importación:  from other_app.views import Home
    2. Añadir una URL a urlpatterns:  path('', Home.as_view(), name='home')
Incluyendo otra configuración de URLs
    1. Importar la función include(): from django.urls import include, path
    2. Añadir una URL a urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
