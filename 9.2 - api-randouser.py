import requests as re
from pydantic import BaseModel  # serializacja danych typu json, bazy danych , podobne
from typing import List

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

class UserInfo(BaseModel):
    name: dict
    email: str
    picture: dict


# user = data['results'][0]  - wyciągneliśmy wewnętrznego jsona z listy w jakiej w jsonie był
# parsujemy tylko ten wewnętrzny
print(user)
# {'gender': 'male', 'name': {'title': 'Mr', 'first': 'Prebislav', 'last': 'Brovchenko'},
#  'location': {'street': {'number': 295, 'name': 'Akademika Iefremova'},
#  'city': 'Yagotin', 'state': 'Kirovogradska',
#  'country': 'Ukraine',
#  'postcode': 95974,
#  'coordinates': {'latitude': '75.4885', 'longitude': '-132.6496'},
#               'timezone': {'offset': '+3:00', 'description': 'Baghdad, Riyadh, Moscow, St. Petersburg'}},
#  'email': 'prebislav.brovchenko@example.com',
#  'login': {'uuid': 'a1805f6f-ff89-4b94-9dde-db2b3e46e19d', 'username': 'ticklishswan876', 'password': 'soccer1',
#            'salt': '07FJTLpM', 'md5': 'e45a6ea02e44e7288624bc58a0f56274',
#            'sha1': '81fadfb7b73f36984495c4b49a60f8555043b874',
#            'sha256': '9bb14c43022a91e19f545a778493d8f50e38cdcd8cc4207426254798aad1d078'},
#  'dob': {'date': '1986-07-16T11:23:20.963Z', 'age': 37}, 'registered': {'date': '2005-11-02T04:44:38.680Z', 'age': 18},
#  'phone': '(067) Y24-8068', 'cell': '(066) X25-5320', 'id': {'name': '', 'value': None},
#  'picture': {'large': 'https://randomuser.me/api/portraits/men/74.jpg',
#              'medium': 'https://randomuser.me/api/portraits/med/men/74.jpg',
#              'thumbnail': 'https://randomuser.me/api/portraits/thumb/men/74.jpg'}, 'nat': 'UA'}

# user = data['results'][0]  - wyciągneliśmy wewnętrznego jsona z listy w jakiej w jsonie był
user_info = UserInfo(**user)  # ** rozpakowanie danych słownikowych na obiekt wskazanej klasy
print(type(user_info))  # user = data['results'][0]  - wyciągneliśmy wewnętrznego jsona z listy w jakiej w jsonie był
print(user_info)
# name = {'title': 'Mr', 'first': 'Prebislav', 'last': 'Brovchenko'}
# email = 'prebislav.brovchenko@example.com'
# picture = {'large': 'https://randomuser.me/api/portraits/men/74.jpg',
#            'medium': 'https://randomuser.me/api/portraits/med/men/74.jpg',
#            'thumbnail': 'https://randomuser.me/api/portraits/thumb/men/74.jpg'}
