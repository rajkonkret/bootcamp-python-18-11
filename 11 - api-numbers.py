import requests

url = 'http://numbersapi.com/random/year?json'

response = requests.get(url)
data = response.json()
print(data)
print(type(data))  # <class 'dict'>
# {'text': '699 is the year that Umayyad troops invade Armenia and secure submission of Smbat VI
# Bagratuni.',
#  'number': 699, 'found': True, 'type': 'year'}
print("Podaj odpowiedź na pytanie:\n", data['text'])
print(data['number'])
