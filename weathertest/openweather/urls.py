from django.urls import path
from . import views

#Para poder acceder a las vistas creadas es necesario mapearlas a una URL, cosa que hace este archivo URLconf

# Cada función path() asocia un patrón URL a una vista específica, que se presenta cuando el patrón se empareja

urlpatterns = [
	path('',views.index,name='index'),
]