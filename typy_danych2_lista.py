# lista - kolekcja przechowująca dowolną ilość danych
# prechowuje różne typy danych w jednej liscie (można mieszac str, int etc...)
# lista zachowuje kolejnośc przy dodawaniu do niej elementów

lista = []  # deklaracja pustej listy
print(lista)  # pusta lista [] - nawiasy kwadratoe, są charakterystyczne dla listy
print(type(lista))  # <class 'list'>
print(bool(lista))  # False dla pustej listy

# deklaracji listy i wypęłnienie jej danymi w miejscu deklaracji
lista2 = [10, 20, 30]
print(type(lista2))  # <class 'list'>
print(lista2)  # [10, 20, 30] - int

lista3 = [10.77, 30.66, 67, 15]
print(type(lista3))  # <class 'list'>
print(lista3)  # [10.77, 30.66, 67, 15] float

# stworzyc listy mieszane, int, str, float
lista_mieszana = [10, 5.2, "Oko"]
print(type(lista_mieszana))  # <class 'list'>
print(lista_mieszana)  # [10, 5.2, 'Oko']

print(len(lista_mieszana))  # 3
# [10, 5.2, 'Oko']
#  0(-3)1(-2)2(-1)

# dodawanie elemntu na końcu listy
lista.append("Radek")
lista.append("MAciek")
lista.append("Tomek")
lista.append("Zenek")
lista.append("Marta")
print(lista)
print(type(lista))  # <class 'list'>
# ['Radek', 'MAciek', 'Tomek', 'Zenek', 'Marta']
#   0(-5)     1(-4)     2(-3)   3(-2)     4(-1)
print(len(lista))  # 5 długosc listy
# wypisanie elemntu z listy
# nazwa listy, nawias kwadratowy, numer indeksu
print(lista[0], lista[-5])
print(lista[1], lista[-4])
print(lista[2], lista[-3])
print(lista[3], lista[-2])
print(lista[4], lista[-1])  # wyswietlenie ostatniego elemntu z listy
# Radek Radek
# MAciek MAciek
# Tomek Tomek
# Zenek Zenek
# Marta Marta
# 10:30