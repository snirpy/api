import requests


api_key = 'dfb53877c237e5af40f8d9df15913ea5'
city_name = 'Clichy'
url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"


response = requests.get(url)
data = response.json()


print(data)



       
