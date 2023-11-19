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
# Podanie indexu spoza zakresu wygeneruje błąd
# print(lista[5])  # IndexError: list index out of range
# print(lista[10])
# Traceback (most recent call last):
#   File "C:\Users\rajko\PycharmProjects\bootcamp-python-18-11\typy_danych2_lista.py", line 54, in <module>
#     print(lista[10])
# IndexError: list index out of range
# []

# Wypisywanie wielu elemntów listy (slice)
# ['Radek', 'MAciek', 'Tomek', 'Zenek', 'Marta']
print(lista[0:3])  # ['Radek', 'MAciek', 'Tomek'] indeksy 0 1 2 - z prawej zakres otwarty
print(lista[1:3])  # ['MAciek', 'Tomek']
print(lista[:3])  # ['Radek', 'MAciek', 'Tomek']
print(lista[:2])  # ['Radek', 'MAciek']
print(lista[-3:])  # ['Tomek', 'Zenek', 'Marta'] - ostatnie 3
print(lista[-2:])  # ['Zenek', 'Marta']
print(lista[-1:])  # ['Marta'] - lista z ostatnim elementem
print(lista[-1])  # Marta  - ostatni elemnt
print(lista[:])  # ['Radek', 'MAciek', 'Tomek', 'Zenek', 'Marta'] - cała lista
print(lista[2:])  # ['Tomek', 'Zenek', 'Marta']
print(lista[-3:0])  # [] pusta lista bo on idzie w prawo, a indeks 0 znajduję sie po lewej stronie od -3
print(lista[7:9])  # [] - pusta lista przy uzyciu indeksów spoza zakresu listy

# nadpisanie elemntu w liscie na indeksie
lista[2] = "Mikołaj"  # nadpisanie trzeciego elementu w liscie
print(lista)  # ['Radek', 'MAciek', 'Mikołaj', 'Zenek', 'Marta']

# rozszerzenie listy, wstawienie elementu w konkretne miejsce(indeks)
lista.insert(1, "Marcin")
print(lista)  # ['Radek', 'Marcin', 'MAciek', 'Mikołaj', 'Zenek', 'Marta']

# usunięcie elementu z listy
# 1. usunięcie po indeksie pop()
# 2. usunięie po elemencie remove()

# usunięci po indeksie pop() - zwraca usunięty element
print(lista.pop(0))  # Radek - usunięty elemnt
print(lista)  # ['Marcin', 'MAciek', 'Mikołaj', 'Zenek', 'Marta']
ind = lista.index('Zenek')  # sprawdzenie numeru indeksu dla danego elementu
print(ind)  # 3
print(lista.pop(ind))  # Zenek
print(lista)  # ['Marcin', 'MAciek', 'Mikołaj', 'Marta']

# usunięcie po elemencie remove()
# lista.remove('Maciek')  # ValueError: list.remove(x): x not in list
# lista.remove('MAciek')
print(lista.remove('MAciek'))  # None - zwraca None
print(lista)  # ['Marcin', 'Mikołaj', 'Marta']

lista.append('MArta')
print('Marta' in lista)  # True
print('MArta' in lista)  # True
print('MAciek' in lista)  # False

print(lista)  # ['Marcin', 'Mikołaj', 'Marta', 'MArta']
lista.append('Marcin')
print(lista)  # ['Marcin', 'Mikołaj', 'Marta', 'MArta', 'Marcin']
print(lista.index('Marcin'))  # zwróci pierszy napotkany 0
lista.remove('Marcin')  # usunięcie pierwszego naptkonaego elemntu Marcin
print(lista)  # ['Mikołaj', 'Marta', 'MArta', 'Marcin']

a = 1
b = 3
a = b
print(a)  # 3
print(b)  # 3
a = 7
print(a)  # 7
print(b)  # 3

lista4 = lista  # a = b kopiuje adres pamieci. kopiuje referencje
lista5 = lista.copy()  # kopiowanie wszystkich elementow listy do nowej listy
print(lista4)
print(lista)
# ['Mikołaj', 'Marta', 'MArta', 'Marcin']
# ['Mikołaj', 'Marta', 'MArta', 'Marcin']
lista4.clear()  # usunięcie wszystkich elemntów z listy, a = 7
print(lista4)  # []
print(lista)  # []
print(lista5)  # ['Mikołaj', 'Marta', 'MArta', 'Marcin']
# id(0 wypisanie id dla elemntu (dla list miejsce w pamięci)
print(id(lista4))  # 2596711491968
print(id(lista))  # 2596711491968
print(id(lista5))  # 2596712109824

liczby = [45, 999, 34, 22, 13.34, 687]
print(liczby)  # [45, 999, 34, 22, 13.34, 687]
print(type(liczby))  # <class 'list'>
liczby.sort()  # sortowanie
print(liczby)  # [13.34, 22, 34, 45, 687, 999]

lista_osoby = ['radek', 'ola', 'agata', 'lena', 'justyna']
lista_osoby.sort()
print(lista_osoby)  # ['agata', 'justyna', 'lena', 'ola', 'radek']

liczby2 = [45, 999, 34, 22, 13.34, 687, "A"]
# nie potrafi posortowac typu int i str
# liczby2.sort()  # TypeError: '<' not supported between instances of 'str' and 'int'

# mozemy posortowac i od razu odwrócic kolekcje
lista_osoby.sort(reverse=True)
print(lista_osoby)  # ['radek', 'ola', 'lena', 'justyna', 'agata']

# mozemy odwrócic kolekcje nie zmieniajac sortowania
lista_osoby.reverse()
print(lista_osoby)  # ['agata', 'justyna', 'lena', 'ola', 'radek']

liczby3 = [3, 8, 5, 12, 1]
liczby3.reverse()
print(liczby3)  # [1, 12, 5, 8, 3]

print(liczby)  # [13.34, 22, 34, 45, 687, 999]
# nadpisac elemnt na indeksie ? czwarty element
# wypisac osytani po indeksach dodatnich i ujenych (sprawdzic długosc listy)
# zrobic slice(wycinanie) jedno dodatnie, jedno ujemne
# uunac z listy po indeksie i po elemncie
