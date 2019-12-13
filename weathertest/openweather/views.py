from django.shortcuts import render

#Aquí se crean las vistas
#Son un tipo de páginas en la app Django que tienen un template y una función específica.

#Para que el template se renderice, se retorna request, que es necesaria para la función render
#y el nombre del archivo template que se quiere mostrar, en este caso el index.html
def index(request):
	return render(request,'openweather/index.html') #retorna el template en el index.html
