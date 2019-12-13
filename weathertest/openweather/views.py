from django.shortcuts import render

#Aqu� se crean las vistas
#Son un tipo de p�ginas en la app Django que tienen un template y una funci�n espec�fica.

#Para que el template se renderice, se retorna request, que es necesaria para la funci�n render
#y el nombre del archivo template que se quiere mostrar, en este caso el index.html
def index(request):
	return render(request,'openweather/index.html') #retorna el template en el index.html
