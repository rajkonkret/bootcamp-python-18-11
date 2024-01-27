import requests as re

url = 'https://randomuser.me/api/'
response = re.get(url)
print(response.text)
data = response.json()
user = data['results'][0]
print(user)
# {'gender': 'male',
# 'name': {'title': 'Mr', 'first': 'Pilar', 'last': 'Manzanares'},
#  'location': {'street': {'number': 1655, 'name': 'Eje vial Rincón'},
#  'city': 'Huanimaro', 'state': 'Veracruz',
#  'country': 'Mexico', 'postcode': 81423,
#  'coordinates': {'latitude': '21.6032', 'longitude': '-152.6747'},
#  'timezone': {'offset': '-9:00', 'description': 'Alaska'}},
#  'email': 'pilar.manzanares@example.com',
#  'login': {'uuid': 'c822a5ec-3ac7-4a77-b7df-f1b8c80aff50', 'username': 'ticklishwolf995', 'password': 'jerry',
#            'salt': 'oPVCQCD9', 'md5': '942caa93c890653aa958b93ab347356b',
#            'sha1': '44f9a227b6baab8385ae9e186c683215449dcd16',
#            'sha256': '7e4ba4ad7bb6b272759260db3c9bcdd823b82f56098145c94f7c35afa85226ed'},
#  'dob': {'date': '1948-10-20T16:58:19.589Z', 'age': 75},
#  'registered': {'date': '2016-10-06T10:26:08.805Z', 'age': 7},
#  'phone': '(675) 069 9306', 'cell': '(672) 847 5219',
#  'id': {'name': 'NSS', 'value': '73 33 15 3650 6'},
#  'picture': {'large': 'https://randomuser.me/api/portraits/men/56.jpg',
#              'medium': 'https://randomuser.me/api/portraits/med/men/56.jpg',
#              'thumbnail': 'https://randomuser.me/api/portraits/thumb/men/56.jpg'}, 'nat': 'MX'}
print(f"Imię: {user['name']['first']}")  # Imię: Clazina
print(f"Nazwisko: {user['name']['last']}")  # Nazwisko: Boerhof
print(f'Email: {user['email']}')  # Email: mads.moller@example.com
photo_url = user['picture']['large']
print(f"Link do zdjęcia: {photo_url}")  # Link do zdjęcia: https://randomuser.me/api/portraits/women/84.jpg

response_photo = re.get(photo_url)
print(type(response_photo))  # <class 'requests.models.Response'>
with open('user_photo.jpg', 'wb') as f:
    f.write(response_photo.content)

print("Zdjęcie zostało zapisane")
# zbudowac schemat klas dla name(first,last), email, picture(large)