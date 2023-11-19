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

tupla5 = "Radek", "Tomek", "Zenek", "Bartek"
tupla6 = ("Radek", "Tomek", "Zenek", "Bartek")  # można tez dodac nawiasy ()
print(type(tupla5))
print(tupla5)  # ('Radek', 'Tomek', 'Zenek', 'Bartek')
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
