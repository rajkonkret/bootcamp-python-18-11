# funkcje - wydizelony program, mamy mozliwosc w dowolnym momncie wywołania
# funkcja przed wywołaniem musi zostastać zdefiniowana

# zmienne globalne
a = 6
b = 7


# definicja funkcji
def dodaj():
    print(a + b)  # przyjeło wartości z globalnego zakresu (scope)
    c = 7  # zdeklarowane wewnątrz funkcji, nie jest widoczne poza funkcją


def dodaj2(a, b):  # argumenty a i b obowiązkowe do przekazania
    # zadeklarowalismy a i b w argumentach funkcji
    # a i b w tym przypadku są to wewnętrzne zmienne dla funkcji
    # zasięg lokalny
    print(a + b)


# Przeciazanie argumentów funkcji
# w pythonie nie dział w klasyczny sposób
# def odejmij(a, b):
#     print(a - b)

# mozemy zasymulowac poprzez wartości domyślne argumentów
def odejmij(a, b, c=0):  # c - argument z domyśłną wartością
    print(a - b - c)


# uzycie funkcji (uruchomienie)
# nazwa funkcji, nawiasy (), ewentualnie w nawiasach wartosci dla argumentów
dodaj()  # 13
# print(c)  # NameError: name 'c' is not defined c jest widoczne tylko wewnątrz funkcji
# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
dodaj2(5, 9)  # 14, przekazanie argumentów do funkcji po pozycji
odejmij(6, 9)  # -3 przekazane a i b, c bedzie domyslne z konstrukcji funkcji=0
odejmij(6, 9, 4)  # -7, przekazane a, b i c, c bedzie równe 4
odejmij(c=9, b=7, a=8)  # argumenty po nazwie

# print(dodaj() + odejmij(5, 7))
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
print(dodaj())  # None
# te funkcje nie zwracją wyniku (print tylko wypisuje)
