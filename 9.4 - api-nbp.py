# http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/
# Komunikacja z serwisem polega na wysłaniu odpowiednio sparametryzowanego żądania HTTP GET
# na adres bazowy http://api.nbp.pl/api/.
# Parametry zapytań o kursy walut
#
# {table} – typ tabeli (A, B, lub C)
# {code} – trzyliterowy kod waluty (standard ISO 4217)  USD, EUR
# {topCount} – liczba określająca maksymalną liczność zwracanej serii danych
# {date}, {startDate}, {endDate} – data w formacie RRRR-MM-DD (standard ISO 8601)
# oczekuje informacji jaki jest dzis kurs euro i dolara
# http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/
# {table} za tekst z klamerkami wstawiamy wartość u nas: A
# {code} za tekst z klamerkami wstawiamy wartość u nas: EUR

import requests as re
from pydantic import BaseModel
from typing import List
from datetime import date

url = 'http://api.nbp.pl/api/exchangerates/rates/A/EUR/'
response = re.get(url)
print(response)  # <Response [200]>
table = response.json()
print(table)
# {'table': 'A', 'currency': 'euro', 'code': 'EUR',
#  'rates': [{'no': '019/A/NBP/2024', 'effectiveDate': '2024-01-26', 'mid': 4.3802}]}
print(table['rates'][0]['mid'])  # 4.3802


# print(table['rates']
# -> lista (wyciagamy pierwszy element)[0]
# -> słownik (wyciągamy po kluczu)['mid'])  # 4.3802

# zamienic na deserializacje na obiekty

class Rate(BaseModel):
    no: str
    # effectiveDate: str
    effectiveDate: date  # 2024-01-26
    mid: float


class CurrencyData(BaseModel):
    table: str
    currency: str
    code: str
    rates: List[Rate]


currency_data = CurrencyData(**table)  # rozpakowanie danych jsona na obiekty klas
print(currency_data)
print(
    f"{currency_data.currency} {currency_data.code} {currency_data.rates[0].mid} {currency_data.rates[0].effectiveDate}")
# euro EUR 4.3802 2024-01-26
