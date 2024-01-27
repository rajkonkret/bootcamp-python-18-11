# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
import requests

# url =  https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
# {API key}
# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
url = ('http://api.openweathermap.org/data/2.5/'
       'weather?q=Warszawa&appid=99a24a78addf4a2c41947189fcff67f7&&lang=p&format=jsonl&units=metric')

page = requests.get(url)
print(page)  # <Response [200]>
print(page.text)  # wyswietla jsona
json = page.json()  # parsowanie (zamiana) jsona(text) na typ słownikowy w pythonie
print(json)  # json zamieniony na słownik
# {'coord': {'lon': 21.0118, 'lat': 52.2298},
#  'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'base': 'stations',
#  'main': {'temp': 2.77, 'feels_like': -2.01, 'temp_min': 2.17, 'temp_max': 3.73, 'pressure': 1016, 'humidity': 91},
#  'visibility': 10000, 'wind': {'speed': 6.17, 'deg': 270}, 'clouds': {'all': 75}, 'dt': 1706349620,
#  'sys': {'type': 2, 'id': 2035775, 'country': 'PL', 'sunrise': 1706336711, 'sunset': 1706368300}, 'timezone': 3600,
#  'id': 756135, 'name': 'Warsaw', 'cod': 200}
print(json['weather'][0]['description'])  # broken clouds
print(json['main']['temp'])  # 2.75
print(json['main']['temp_min'])  # 2.17
print(json['main']['temp_max'])  # 3.73
print(json['name'])  # Warsaw
