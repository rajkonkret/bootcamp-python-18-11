# krotka (tuple) - niezmienna lista
# jednoelementowa krotka - zmiennej, niezmmiennej czyli stałej

tupla1 = "radek"
print(type(tupla1))  # <class 'str'>
tupla2 = ("radek")
print(type(tupla2))  # <class 'str'>
# Żeby python uznał, ze ma tuple musi byc w takiej formie
tupla3 = "radek",  # jednoelemntowa tupla musi miec przecinek po pierwszym elemencie
tupla4 = ("radek",)  # Forma z nawiasami () zalecana dla tupli jednoelemntowej przez PEP8
print(type(tupla3))  # <class 'tuple'>
print(type(tupla4))  # <class 'tuple'>

tupla_names = "Radek", "Tomek", "Zenek", "Bartek"
tupla6 = ("Radek", "Tomek", "Zenek", "Bartek")  # można tez dodac nawiasy ()
print(type(tupla_names))
print(tupla_names)  # ('Radek', 'Tomek', 'Zenek', 'Bartek')
temp = 36, 6  # UWAGA: To nie jest float!!!
print(temp)  # (36, 6)
print(type(temp))  # <class 'tuple'>

tupla_liczby = 43, 55, 22.34, 11, 200
print(type(tupla_liczby))  # <class 'tuple'>
print(tupla_liczby)  # (43, 55, 22.34, 11, 200)

# tuple są imutable (niemodyfikowalne) - nie można zmieniac wartości
# temp[0] = 1  # TypeError: 'tuple' object does not support item assignment

# del - usunięcie elemntu z tupli wygeneruje błąd
# del temp[0]  # TypeError: 'tuple' object doesn't support item deletion

# można usunąc całą tuple z pamięci
del temp
# 13:15
print(tupla_liczby[0])  # 43
# pobróbujcie z slice (wycinaniem)  z tupli
print(tupla_liczby[1:3])
print(tupla_liczby[:3])
print(tupla_liczby[0:3])
print(tupla_liczby[2:])
# wypisanie ostatniego elemntu z tupli
print(tupla_liczby[-1])  # 200
print(tupla_liczby[-1::-1])  # (200, 11, 22.34, 55, 43)
# [start:stop:krok] krok -1 idź do tyłu
# [1:4:2]  start=1, stop=4, krok=2
# (43, 55, 22.34, 11, 200)
print(tupla_liczby[1:4:2])  # (55, 11) wyswietla co drugi element
# [-1::-1] - start=-1, stop=poczatek(0) krok=-1 - krok w tył co jeden
print(tupla_liczby[:])  # (43, 55, 22.34, 11, 200) - wyswietlenie całości

print(tupla_names)  # ('Radek', 'Tomek', 'Zenek', 'Bartek')
print("Radek" in tupla_names)  # True
# zadanie domowe - stworzyc takie tuple i posprawdzac obecnosc elemntow

# count() - zlicza ilośc wystąpienia elemntu w krotce
print(tupla_names.count("Tomek"))  # 1 Tomek występuje raz w tupli

# index() - zwraca numer indeksu dla danego elemntu
print(tupla_names.index("Radek"))  # 0 indeks dla elemntu "Radek" jest 0

# sorted() - sortowanie kolekcji
# wyswietlenie posortowanych elementów z tupli
print(sorted(tupla_names))  # ['Bartek', 'Radek', 'Tomek', 'Zenek'] posortowało i zwróciło listę
# posortowac i odwrócić kolejność
print(sorted(tupla_names, reverse=True))  # ['Zenek', 'Tomek', 'Radek', 'Bartek']

# rozpakowanie tupli
a, b = 1, 2
print(type((1, 2)))  # <class 'tuple'>
print(a)
print(b)
# a, b = 1, 2, 3  # ValueError: too many values to unpack (expected 2)
a, *b = 1, 2, 3  # dołozenie * powoduje, ze mamy taki worek na pozostałe dane
print(a)  # 1
print(b)  # [2, 3]

# ('Radek', 'Tomek', 'Zenek', 'Bartek')
# dodajemy * do dowolnego elemntu, * moze byc tylko raz użyta
imie1, *imie2, imie3 = tupla_names
# pierwszy worek ostani
print(imie1, imie2, imie3)  # Radek ['Tomek', 'Zenek'] Bartek
# ('Bartek', 'Radek', 'Tomek', 'Zenek')
#   imie1        *imie2         imie3
# Przecwiczyc wariant * przy imie1
# * przy imie3
*imie1, imie2, imie3 = tupla_names  # ('Radek', 'Tomek', 'Zenek', 'Bartek')
# worek, przedostani, ostatni
print(imie1, imie2, imie3)  # ['Radek', 'Tomek'] Zenek Bartek

imie1, imie2, *imie3 = tupla_names  # ('Radek', 'Tomek', 'Zenek', 'Bartek')
print(imie1, imie2, imie3)  # Radek Tomek ['Zenek', 'Bartek']
# Tam gdzie * tam jest worek na pozostałe, bez * podstawia dane wg kolejności

tupla_paulina = ["Ola", 'Ania', 'Ada', 'Gabi', 'Kasia', 'Paulina']
i1, *i2, i3, i4 = tupla_paulina
# pierwszy worek przedostatni ostatni
# "Ola", worek=['Ania','Ada','Gabi], 'Kasia', 'Paulina'
print(i1, i2, i3, i4)  # Ola ['Ania', 'Ada', 'Gabi'] Kasia Paulina
print("Jeden", "Dwa", "Trzy")  # Jeden Dwa Trzy - dodał automatycznie spacje pomiedzy elementami
# przy wypisywaniu po przecinku
"""
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space. - znak oddzielajacy elementy (domyślnie=' ')
    end:   string appended after the last value, default a newline. - znak nowej linii '\n' - nowa linia
    flush: whether to forcibly flush the stream.
    """
print("Jeden", "Dwa", "Trzy", sep='', end='')  # '' - pusty separator -> JedenDwaTrzy
# end='' znak nowej lini ustawiony na pusty ''
print("Jeden", "Dwa", "Trzy", sep=';')  # ';' - pusty separator -> Jeden;Dwa;Trzy
# JedenDwaTrzyJeden;Dwa;Trzy - wyswietlił w nowej linii
print("Radek", end='')
print("Zenek", end='')
print()  # dostawiamy pusty print by dodał nowa linie, przejdzie do nowej linii
print("Tomek")
# sep:   string inserted between values, default a space. - znak oddzielajacy elementy (domyślnie=' ')
# end:   string appended after the last value, default a newline. - znak nowej linii '\n' - nowa linia
# RadekZenek
# Tomek

lista = list(tupla_names)  # zamiana (rzutowanie) tupli na liste
print(lista)  # ['Radek', 'Tomek', 'Zenek', 'Bartek']
print(type(lista))  # <class 'list'>
