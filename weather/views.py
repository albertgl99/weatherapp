from django.shortcuts import render
import requests

# Función para obtener los datos del clima
def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = "08d2bdd91138b80a2ddb608bc8b8dc34"
    parameters = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=parameters)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Vista principal
def weather_view(request):
    city = request.GET.get('city', 'London')  # Ciudad predeterminada
    weather_data = get_weather(city)

    if weather_data:
        context = {
            'city': city,
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'icon': weather_data['weather'][0]['icon'],
        }
    else:
        context = {
            'city': city,
            'temperature': 'N/A',
            'description': 'Could not retrieve weather data.',
            'icon': '',
        }

    return render(request, 'weather/index.html', context)
