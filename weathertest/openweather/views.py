from django.shortcuts import render

import requests #Se instala esta librería para poder llamar APIs en la app

#Aquí se crean las vistas
#Son un tipo de páginas en la app Django que tienen un template y una función específica.

#Para que el template se renderice, se retorna request, que es necesaria para la función render
#y el nombre del archivo template que se quiere mostrar, en este caso el index.html
def index(request):
	currentWeather_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=5fec5a0ae12df556297c8080de1a434a' #Para utilizar el current API de OpenWeather
	# en unidades métricas y con el API Key gratuito que se adquiere al registrarse en OpenWeather
	nextDays_url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&appid=5fec5a0ae12df556297c8080de1a434a' #Para utilizar el 5 days forecast API
	#no se usa el API de 16 days forecast por lo que solo funciona para suscripciones pagas. La desventaja del 5 days forecast es que da el clima cada 3horas
	#entonces no coincidirían siempre el current con la información del 5 days
	#city = 'valledupar'
	#request.GET es un diccionario que contiene todos los parámetros de solicitud GET(específicos de Django)
	#El método get() devuelve un value para la key dada si la esta está en el diccionario. Si no, tiene default 'valledupar'.
	#request.GET.get() es una combinación de estas que utiliza keys / values de un GET request a la que se puede acceder
	city=request.GET.get('city','valledupar')
	if not city:
		city = 'valledupar' #en caso de que el usuario toque el botón de buscar y no escriba ninguna ciudad manda default 'valledupar'
	weather_info = requests.get(currentWeather_url.format(city)).json() #Se envía el request a la URL con una ciudad y recibe los datos en JSON de esa ciudad
	# se pasan a JSON por lo que este tipo de objetos son facilmente representados como diccionarios y listas en Python
	#Se crea un diccionario para pasar los datos que se requieran al template para que el usuario los vea
	weather = {
		'city' : city,
		'temperature' : weather_info['main']['temp'],
		'description' : weather_info['weather'][0]['description'], 
		'icon' : weather_info['weather'][0]['icon'],
	}# 'main' es un diccionario y 'weather' una lista de 1 solo objeto
	
	next_data = [] #se crea una lista vacía en donde se almacenarán los datos de los siguientes días
	#Se usa un for loop por lo que se tomarán más de 1 dato en este caso

	for i in range(6):
		nextWeather_info = requests.get(nextDays_url.format(city)).json()
		next_weather = {
			'temperature' : nextWeather_info['list'][i]['main']['temp'],
			'speed' : nextWeather_info['list'][i]['wind']['speed'],
			'pressure' : nextWeather_info['list'][i]['main']['pressure'],
			'icon' : nextWeather_info['list'][i]['weather'][0]['icon'],
		}
		next_data.append(next_weather)
	context = {'weather' : weather, 'next_data' : next_data}
	#context es un diccionario de valores para agregar al template a través de la función render. Por defecto viene vacío
	#retorna el template en el index.html
	return render(request,'openweather/index.html', context) 
