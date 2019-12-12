from django.shortcuts import render

from django.http import HttpResponse

#Aquí se crean las vistas
#Son un tipo de páginas en la app Django que tienen un template y una función específica.

def index(request):
	return HttpResponse("Test message on the openweather app index.") #la vista index mostraría el mensaje al abrir la aplicación
