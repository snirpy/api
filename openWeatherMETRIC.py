import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',  # Ajout du paramètre units=metric
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            # Traitement des données de la réponse
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            print(f"Temperature in {city}: {temperature}°C, {description}")
        else:
            print(f"Erreur {response.status_code}: {data['message']}")

    except Exception as e:
        print(f"Erreur lors de la requête : {str(e)}")

# Remplacez 'YOUR_API_KEY' par votre clé API OpenWeatherMap
api_key = 'YOUR_API_KEY'
city = 'Paris'

get_weather(api_key, city)
