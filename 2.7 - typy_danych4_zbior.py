# set - przechowuje niepowtarzające sie elementy
# nie zachowuje kolejnosci przy dodawaniu elementów

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)  # rzutowanie (zamiana) listy na set
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}
lista2 = list(zbior)  # zamiana na liste
print(lista2)
lista2.remove(11)
print(lista2)
# usuniecie powtarzających się elemnetów w liscie - utrata kolejności
# [44, 55, 66, 777, 33, 22, 11, 33, 11]
# [33, 66, 777, 11, 44, 22, 55]
# [33, 66, 777, 44, 22, 55]

# utworzzenie pustego seta - zbioru
# dla pustej listy uzywalismy pustych nawiasó kwadratowych []
# pusty set musimy utworzyc za pomocą słowka set() z nawiasami
zb2 = set()
print(zb2)  # set() pusty set wyswietli sie tak: set()
print(type(zb2))  # <class 'set'>

# dodanie elemntów do zbioru
zb2.add(2)
zb2.add(3)
zb2.add(5)
zb2.add(5)
zb2.add(3)
print(zb2)  # {2, 3, 5}

# {33, 66, 777, 11, 44, 22, 55}
zbior.add(33)
zbior.add(18)
zbior.add(18)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55}
# pop() - usunięcie elementu ze zbioru
# nie mmozemy podac numeru indeksu
print(zbior.pop())  # 33, usunie pierwszy element ze zbioru
print(zbior)  # {66, 777, 11, 44, 18, 22, 55}
print(zbior.pop())  # 66
# Za każdym użyciem pop() usuniemy kolejny pierwszy element
zbior.pop()
zbior.pop()
print(zbior)  # {44, 18, 22, 55}
# sortowanie zbioru nie jest mozliwe
# mozna posortowac i zwrócic jako liste
print(sorted(zbior))  # [18, 22, 44, 55] zwroci dla zbioru posortowaną liste

# ze zbioru można usunąc konkretny element
# remove()
zbior.remove(55)
zbior.remove(18)
print(zbior)  # {44, 22}

# tworzenie zbioru z konkretnymi elementami w miejscu deklaracji
zbior2 = {667, 11, 44, 18, 52, 22, 667, 62, 999}
print(zbior2)  # {999, 11, 44, 18, 52, 22, 667, 62} - do pamieci zapisał bez powtórzeń

# suma zbiorów
print(zbior | zbior2)  # suma zbiorów {999, 11, 44, 18, 52, 22, 667, 62}
# suma - wszystko to co znajduje sie w zbiorze i w zbiorze2
# uwzględniając to, że nie powtórzą sie
# {44, 22} | {999, 11, 44, 18, 52, 22, 667, 62} = {999, 11, 44, 18, 52, 22, 667, 62}
print(zbior.union(zbior2))  # {999, 11, 44, 18, 52, 22, 667, 62} - ta sama operacja
# po wykonaniu tych operacji zbiory żródlowe zachowują swoje dane
print(zbior)  # {44, 22}
print(zbior2)  # {999, 11, 44, 18, 52, 22, 667, 62}
zbior3 = {8, 9, 10}
print(zbior.union(zbior2, zbior3))  # {999, 8, 9, 10, 11, 44, 18, 52, 22, 667, 62} - suma trzech zbiorów

# część wspólna
print(zbior & zbior2)  # {44, 22} - te elementy znajdują sie zarówno zbiorze jak i w zbiorze2

# róznica zbiorów
print(zbior - zbior2)  # set()
# {44, 22} - {999, 11, 44, 18, 52, 22, 667, 62} = pusty zbiór bo elemnty 44 i 22 znajduja sie w zbiorze2

print(zbior2 - zbior)  # {999, 11, 18, 52, 667, 62}
# {999, 11, 44, 18, 52, 22, 667, 62} - {44, 22} = {999, 11, 18, 52, 667, 62}
print(zbior2.difference(zbior))  # ten sam wynik {999, 11, 18, 52, 667, 62}

zbior4 = zbior2.copy()  # kopiowanie elementów zbioru
print(zbior4)  # {999, 11, 44, 18, 52, 22, 667, 62}
zbior2.clear()  # czyszczenie wszystkich elemntów ze zbioru2
print(zbior4)  # {999, 11, 44, 18, 52, 22, 667, 62}
print(zbior2)  # set() - zbior2 pusty, zbiór4 zachował elemnty

# wrzucenie zawartosci innego zbioru do drugiego zbioru
zbior2.update(zbior4)  # podobne do union, taka suma zbiorów
print(zbior2)  # {999, 11, 44, 18, 52, 22, 667, 62}
