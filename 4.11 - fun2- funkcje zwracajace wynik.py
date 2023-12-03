# funkcje zwracające wynik
# musza byc zakonczone słowem return

def dodaj(a, b):
    return a + b  # funkcja zwraca wynik


def odejmij(a=0, b=0, c=0):  # trzy argumenty z wartościami domyślnymi
    return a - b - c


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(dodaj(6, 9))
print(dodaj(5, 6) + dodaj(23, 78))  # 112
print(odejmij())
print(odejmij(1, 2))
print(odejmij(1, 2, 3))
print(odejmij(b=7, c=9))  # -16
print(odejmij(1, b=7, c=9))  # -15

print(oblicz_vat(1000))
print(oblicz_vat(1000, 7))
print(oblicz_vat(vat=8, cena=1000))
# 1230.0
# 1070.0
# 1080.0

obl = oblicz_vat(1000)
print(obl)
print(type(obl))  # <class 'float'>
if obl == 1230:
    print("Działa")  # Działa
