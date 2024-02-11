# Decimal -  typ danych pozwalajacy ominac i pracowac z błedem zaokraglenia
from decimal import Decimal

"""
    Construct a new Decimal object. 'value' can be an integer, string, tuple,
    or another Decimal object. If no value is given, return Decimal('0'). The
    context does not affect the conversion and is only passed to determine if
    the InvalidOperation trap is active.
    """

# deklaracja liczb typy Decimal
kwota1 = Decimal('10.25')
kwota2 = Decimal('5.50')
precyzja2 = Decimal('0.00')

# dodawanie kwot
suma = kwota1 + kwota2
print("Suma:", suma)  # Suma: 15.75

# odejmowanie
roznica = kwota1 - kwota2
print("Różnica:", roznica)  # Różnica: 4.75
print("Różnica:", roznica.quantize(precyzja2))  # Różnica: 4.75

# mnożenie
podatek = Decimal('0.23')
kwota_z_podatkiem = kwota1 * (1 + podatek)
print("Kwota z podatkiem:", kwota_z_podatkiem)  # Kwota z podatkiem: 12.6075
print("Kwota z podatkiem:", kwota_z_podatkiem.quantize(precyzja2))  # Kwota z podatkiem: 12.61

# dzielenie
ilosc_osob = 3
rachunek_na_osobe = kwota_z_podatkiem / ilosc_osob
print("Rachunek na osobe:", rachunek_na_osobe.quantize(precyzja2))  # Rachunek na osobe: 4.20

precyzja = Decimal('0.001')
a = Decimal('1.2345')
b = Decimal('2.3456')
c = a + b
print(c)
print(c.quantize(precyzja))
# 3.5801
# 3.580
