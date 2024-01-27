import requests
from pydantic import BaseModel  # serializacja danych typu json, bazy danych , podobne
from typing import List

# url = 'https://restcountries.com/v3.1/name/{name}?fullText=true'
url = 'https://restcountries.com/v3.1/name/Poland'

response = requests.get(url)
print(response)  # <Response [200]>
# sprawdzic jaka odpowiedź przyszła z serwera
# odczytac wybrne dane
# name -> common, official
# capital
# population
print(response.text)  # wypisanie czystego jsona
data = response.json()  # parsowanie (zamiana) odpowiedzi z jsona na słownik pythonowy
print(type(data))  # sprawdzenie typu
print(data[0])  # wyciągnięcie pierwszego elementu z listy
country = data[0]
print(f"Nazwa kraju: {country['name']}")
# {'common': 'Poland', 'official': 'Republic of Poland',
# 'nativeName': {'pol': {'official': 'Rzeczpospolita Polska', 'common': 'Polska'}}}
print(f"Nazwa główna: {country['name']['common']}")  # Nazwa główna: Poland
print(f"Nazwa oficjalna: {country['name']['official']}")  # Nazwa oficjalna: Republic of Poland
# "capital": [
#       "Warsaw"
#     ]
print(f"Stolica kraju: {country['capital']}")  # Stolica kraju: ['Warsaw']
print(f"Stolica kraju: {country['capital'][0]}")  # Stolica kraju: Warsaw
# "population": 37950802,
print(f"Liczba ludności: {country['population']}")  # Liczba ludności: 37950802


class Name(BaseModel):
    common: str
    official: str
    nativeName: dict


class CountryInfo(BaseModel):
    # name: dict  # pobieramy jako słownik by zobaczyć co tam jest
    name: Name  # teraz ustawiamy jako klasa Name
    capital: List[str]
    population: int


country_data = [CountryInfo(**data) for data in response.json()]
# tworzymy listę z obiektów jsona bo dostalismy JsonArray
for country in country_data:
    print(country)
    # name={'common': 'Poland', 'official': 'Republic of Poland',
    # 'nativeName': {'pol': {'official': 'Rzeczpospolita Polska', 'common': 'Polska'}}}
    # capital=['Warsaw'] population=37950802
    print(type(country))  # <class '__main__.CountryInfo'>
    print(country.name)
    # {'common': 'Poland', 'official': 'Republic of Poland',
    # 'nativeName': {'pol': {'official': 'Rzeczpospolita Polska', 'common': 'Polska'}}}
    print(type(country.name))  # <class '__main__.Name'>
    print(country.name.common)  # Poland
    print(country.population)
    print(country.capital)  # ['Warsaw']
    print(country.name.nativeName)
    # {'pol': {'official': 'Rzeczpospolita Polska', 'common': 'Polska'}}
