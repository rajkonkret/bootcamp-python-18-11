# REST API - sposób komunikowanie się i wymiany danych pomiędzy klientem a serwerem
# klient - przeglądarka
# serwer - tzw backend, serwer który ma wystawione metody potrafiace obsłużyc żadania klienta
# na stronie guzik - zapisz usera -> save_user -> (json) -> zapisac do bazy danych jako rekordy w tabelkach
# GET, POST, PUT/PATCH, DELETE - metody http
# GET - pobiera dane
#
# Pobiera określony zasobu według podanego identyfikatora.

# POST  - np za pomoca jsona w body - wysyła dane do serweera np do zapisu do bazy
#
# Tworzy nowy zasób.
# Jest wykorzystywany do wszystkich innych operacji, które nie wpisują się w ramy innych metod.
# Może służyć do pobierania danych w przypadku kiedy musimy w ramach body dostarczyć dodatkowe parametry.

# PUT - aktualizuje obiekt ale praktycznie w całosci
#
# Aktualizuje dany zasób na podstawie podanego identyfikatora.
# Może służyć do tworzenia nowego zasobu jeśli jego identyfikator jest znany.

# DELETE - usniecia danego obiektu systemu
#
# Usuwa określony zasób według identyfikatora.

# PATCH - aktualizuje element obiektu(np.: adres email)
#
# Aktualizuje część wskazanego zasobu.
# Od PUT’a różni się tym, że aktualizuje jedynie część zasobu.
# metody http odpowiadają operacji na bazie danych:
# GET - SELECT , POST - INSERT, PUT - UPDATE, DELETE - DELETE
# CRUD - CREATE, READ, UPDATE, DELETE - http-> POST, GET, PUT/PATCH, DELETE
# klientem może byc aplikacja pythonowa potrafiaca korzystac z metod http i zasad REST API (np.: json)
import requests  # słuzy do komunikacji http w pythonie
from pydantic import BaseModel  # serializacja danych typu json, bazy danych , podobne
from typing import List

url = 'http://api.open-notify.org/astros.json'
response = requests.get(url)
print(response)
# <Response [200]> ok  200 - status komunikacji
# 3xx - błedy przekierowania
# 4xx - 404 - brak zasobu, 400 Bad Request - błedne dane
# 5xx - błedy po stronie serwera - baza wywaliła sie
print(response.text)  # str
response_data = response.json()  # zamiana jsona na słownik
print(type(response_data))  # <class 'dict'>

for k, v in response_data.items():
    print(k, "=>", v)
# message => success
# people => [{'name': 'Jasmin Moghbeli', 'craft': 'ISS'},
# {'name': 'Andreas Mogensen', 'craft': 'ISS'},
# {'name': 'Satoshi Furukawa', 'craft': 'ISS'},
# {'name': 'Konstantin Borisov', 'craft': 'ISS'},
# {'name': 'Oleg Kononenko', 'craft': 'ISS'},
# {'name': 'Nikolai Chub', 'craft': 'ISS'},
# {'name': "Loral O'Hara", 'craft': 'ISS'}]
# number => 7
print(response_data['message'])
for i in response_data['people']:
    print(i)
# {'name': 'Jasmin Moghbeli', 'craft': 'ISS'}
# {'name': 'Andreas Mogensen', 'craft': 'ISS'}
# {'name': 'Satoshi Furukawa', 'craft': 'ISS'}
# {'name': 'Konstantin Borisov', 'craft': 'ISS'}
# {'name': 'Oleg Kononenko', 'craft': 'ISS'}
# {'name': 'Nikolai Chub', 'craft': 'ISS'}
# {'name': "Loral O'Hara", 'craft': 'ISS'}

# wyswietlic z tej listy imie nazwisko osoby  bedacej na miejscu 3 w liscie
print(response_data['people'][2]['name'])  # Satoshi Furukawa


class Astronaut(BaseModel):
    name: str
    craft: str


class AstroData(BaseModel):
    message: str
    people: List[Astronaut]
    number: int


# rozpakowanie danych z jsona na obiekty klasy
data = AstroData(**response.json())
print(data)
# message = 'success'
# people = [Astronaut(name='Jasmin Moghbeli', craft='ISS'), Astronaut(name='Andreas Mogensen', craft='ISS'),
#           Astronaut(name='Satoshi Furukawa', craft='ISS'), Astronaut(name='Konstantin Borisov', craft='ISS'),
#           Astronaut(name='Oleg Kononenko', craft='ISS'), Astronaut(name='Nikolai Chub', craft='ISS'),
#           Astronaut(name="Loral O'Hara", craft='ISS')]
# number = 7
print(data.message)
print(data.number)
print(data.people)
for people in data.people:
    print(people)
    print(people.name)

# name='Jasmin Moghbeli' craft='ISS'
# Jasmin Moghbeli
# name='Andreas Mogensen' craft='ISS'
# Andreas Mogensen
# name='Satoshi Furukawa' craft='ISS'
# Satoshi Furukawa
# name='Konstantin Borisov' craft='ISS'
# Konstantin Borisov
# name='Oleg Kononenko' craft='ISS'
# Oleg Kononenko
# name='Nikolai Chub' craft='ISS'
# Nikolai Chub
# name="Loral O'Hara" craft='ISS'
# Loral O'Hara
