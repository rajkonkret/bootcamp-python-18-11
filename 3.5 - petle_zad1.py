# for  - petla iteracyjna
import random
from itertools import zip_longest

for i in range(10):  # 0..9
    print(i, i, sep=":")

for i in range(10):
    print(i)

for i in range(10):
    print(i, end="")  # 0123456789 wszystko w jednej linii

print()
print("Koniec pętli")
for i in range(1, 25):  # 1..24
    print(i)

my_string = "Radek"
for i in my_string:
    print(i)

# przerobic zadanie lotto na uzycie pętli
print("----------------------------")
# maszyna lotto
lista_lotto = list(range(1, 50))  # lista liczb od 1 do 49
# print(lista_lotto)
liczby_wylosowane = []
for i in range(6):
    wyn = random.choice(lista_lotto)
    lista_lotto.remove(wyn)
    print(wyn)
    liczby_wylosowane.append(wyn)

print(liczby_wylosowane)

# niema zmienna
for _ in range(4):
    print("Radek")
    # print(_) # Radek

# posortowac i odwrocic liczby_wylosowane
liczby_wylosowane.sort(reverse=True)
print(liczby_wylosowane)  # [39, 24, 16, 15, 12, 2]

for i in range(10):
    if i % 2 == 0:  # % reszta z dzielenia
        print(i, "jest parzyste")
# 0 jest parzyste
# 2 jest parzyste
# 4 jest parzyste
# 6 jest parzyste
# 8 jest parzyste

lista3 = [j for j in range(1, 10) if j % 2 == 0]
print(lista3)  # [2, 4, 6, 8]

# iterowac po kolekcji
for c in lista3:
    if c == 2:
        c += 1  # c = c + 1
    print(c)

a = 1
a += 1  # a = a + 1
print(a)  # 2
a -= 1  # a = a - 1
print(a)  # 1
a *= 2  # a = a * 2
print(a)  # 2
a /= 2  # a = a / 2
print(a)  # 1.0
a %= 2  # a = a % 2
print(a)

# hackerrank

imiona = ['Radek', 'Asia', 'Zbyszek', 'Marcin']

for p in imiona:
    print(p)
# Radek
# Asia
# Zbyszek
# Marcin

# wyswietlic imiona z listy w taki sposob
# 0 Radek
# 1 Asia

for i in range(len(imiona)):  # 4 elementy zakres range(4) -> 0,1,2,3
    print(i, imiona[i])

for i in imiona:
    print(imiona.index(i), i)
# 0 Radek
# 1 Asia
# 2 Zbyszek
# 3 Marcin

# enumerate() - zwraca elemnt kolekcji i jego numer
for p in enumerate(imiona):
    print(p)  # (3, 'Marcin')

a, b = 1, 2

for p, o in enumerate(imiona):
    print(p, o)

for p, o in enumerate(imiona, start=1):
    print(p, o)
# 1 Radek
# 2 Asia
# 3 Zbyszek
# 4 Marcin

ludzie = ['Radek', 'Janek', 'Tomek', 'Martyna', "Marek"]
wiek = [45, 40, 18, 26]
# wypisaniu imienia i odpowiadjacego mu wieku

# for x in range(len(ludzie)):
#     print(ludzie[x], wiek[x])
# # nie zadziała bo rózna długośc list IndexError: list index out of range

# zip() - łączenie sekwencji
for i in zip(ludzie, wiek):
    print(i)  # ('Martyna', 26)

for p, w in zip(ludzie, wiek):
    print(p, w)
# Radek 45
# Janek 40
# Tomek 18
# Martyna 26
# dodac indeks
for i in enumerate(zip(ludzie, wiek)):
    print(i)  # (3, ('Martyna', 26))
a, b = (3, ('Martyna', 26))
print(a)
print(b)  # ('Martyna', 26)
c, d = b
print(c)
print(d)
for a, (c, d) in enumerate(zip(ludzie, wiek)):
    print(a, c, d)
# 0 Radek 45
# 1 Janek 40
# 2 Tomek 18
# 3 Martyna 26

zipped = zip_longest(ludzie, wiek, fillvalue="NONE")
print(type(zipped))  # <class 'itertools.zip_longest'>
zipped_list = list(zipped)
zipped_krotka = tuple(zipped_list)
for name, age in zipped_list:
    print(name, age)

print("*************")
for a, b in zipped_list:
    print(a, b)

print(zipped_krotka)
for name, age in zipped_krotka:
    print(name, age)

for index, (name, age) in enumerate(zipped_krotka):
    print(index, name, age)
# 0 Radek 45
# 1 Janek 40
# 2 Tomek 18
# 3 Martyna 26
# 4 Marek NONE
