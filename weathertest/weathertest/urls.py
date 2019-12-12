"""weathertest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include

#La lista urlpatterns define inicialmente una función que mapea todos los URLs con el patrón admin/ 
#que contiene las definiciones de mapeos URL propios de la aplicación de Administración
#Aqui se apunta el URLconf raíz al módulo url de la app

#La función include () permite hacer referencia a otros URLconfs. Cada vez que Django encuentra include (),
#corta cualquier parte de la URL que coincida hasta ese punto y envía la cadena restante a la URLconf incluida para procesar posteriormente
urlpatterns = [
	path('openweather/', include('openweather.urls')),
    path('admin/', admin.site.urls),
]
