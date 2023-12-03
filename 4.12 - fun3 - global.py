# uzycie global

a = 10
b = 10


def dodaj():
    a = 6  # zmienne lokalne
    b = 7  # nie zmieniaja wartości zmiennych globalnych o tej samej nazwie
    print(a + b)


def dodaj2():
    print(a + b)  # korzysta ze zmiennych globalnych


def dodaj3():
    global a  # oznacza, ze w tej zmiennej ma zasieg globalny
    a = 5  # zostało nadpisane globalne a
    b = 8
    print(a + b)


print(f"Zmienna a, b z góry (globalna): {a}, {b}")  # Zmienna a, b z góry (globalna): 10, 10
dodaj()  # 13
# dodaj(4, 5)  # TypeError: dodaj() takes 0 positional arguments but 2 were given
print(f"Zmienna a, b z góry (globalna): {a}, {b}")  # Zmienna a, b z góry (globalna): 10, 10
dodaj2()  # 20
print(f"Zmienna a, b z góry (globalna): {a}, {b}")  # Zmienna a, b z góry (globalna): 10, 10
dodaj3()  # 13
print(f"Zmienna a, b z góry (globalna): {a}, {b}")  # Zmienna a, b z góry (globalna): 5, 10
dodaj2()  # 15, ta funkcja korzysta z globalnej wartosci a i b
print(f"Zmienna a, b z góry (globalna): {a}, {b}")  # Zmienna a, b z góry (globalna): 5, 10
