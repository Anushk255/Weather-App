import requests

city_name = 'Lucknow'
API_key = '1a4689395c0923691c3689474e1d209b'

url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    print("City:", data['name'])
    print("Weather:", data['weather'][0]['description'])
    print("Temperature:", data['main']['temp'], "°C")
else:
    print("Error:", response.status_code)