from django.shortcuts import render

import requests #Se instala esta librería para poder llamar APIs en la app

#Aquí se crean las vistas
#Son un tipo de páginas en la app Django que tienen un template y una función específica.

#Para que el template se renderice, se retorna request, que es necesaria para la función render
#y el nombre del archivo template que se quiere mostrar, en este caso el index.html
def index(request):
	currentWeather_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=5fec5a0ae12df556297c8080de1a434a' #Para utilizar el current API de OpenWeather
	# en unidades métricas y con el API Key gratuito que se adquiere al registrarse en OpenWeather
	city = "Valledupar"
	weather_info = requests.get(currentWeather_url.format(city)).json() #Se envía el request a la URL con una ciudad y recibe los datos en JSON de esa ciudad
	# se pasan a JSON por lo que este tipo de objetos son facilmente representados como diccionarios y listas en Python
	#Se crea un diccionario para pasar los datos que se requieran al template para que el usuario los vea
	weather = {
		'city' : city,
		'temperature' : weather_info['main']['temp'],
		'description' : weather_info['weather'][0]['description'], 
		'icon' : weather_info['weather'][0]['icon'],
	}
	# 'main' es un diccionario y 'weather' una lista de 1 solo objeto
	context = {'weather' : weather}
	#context es un diccionario de valores para agregar al template a través de la función render. Por defecto viene vacío
	return render(request,'openweather/index.html', context) #retorna el template en el index.html
