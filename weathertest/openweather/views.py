from django.shortcuts import render

from django.http import HttpResponse

#Aqu� se crean las vistas
#Son un tipo de p�ginas en la app Django que tienen un template y una funci�n espec�fica.

def index(request):
	return HttpResponse("Test message on the openweather app index.") #la vista index mostrar�a el mensaje al abrir la aplicaci�n
