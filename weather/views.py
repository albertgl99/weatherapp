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
            'city': weather_data['name'],
            'country': weather_data['sys']['country'],
            'temperature': weather_data['main']['temp'],
            'feels_like': weather_data['main']['feels_like'],
            'min_temp': weather_data['main']['temp_min'],
            'max_temp': weather_data['main']['temp_max'],
            'humidity': weather_data['main']['humidity'],
            'pressure': weather_data['main']['pressure'],
            'wind_speed': weather_data['wind']['speed'],
            'wind_direction': weather_data['wind'].get('deg', 'N/A'),  # Dirección del viento
            'weather': weather_data['weather'][0]['main'],
            'description': weather_data['weather'][0]['description'],
            'icon_url': f"https://openweathermap.org/img/wn/{weather_data['weather'][0]['icon']}@2x.png",
            'sunrise': weather_data['sys']['sunrise'],  # Tiempo de amanecer
            'sunset': weather_data['sys']['sunset'],    # Tiempo de atardecer
            'visibility': weather_data.get('visibility', 'N/A'),  # Visibilidad en metros
        }
    else:
        context = {
            'city': city,
            'temperature': 'N/A',
            'description': 'Could not retrieve weather data.',
            'icon': '',
        }

    return render(request, 'weather/index.html', context)
