wiek = 47  # int
rok = 2023  # int
temp = 36.6  # float - zmiennoprzecinkowe

print(temp)
print(type(temp))  # <class 'float'>

print(wiek + rok)
print(wiek - rok)
print(wiek * rok)
print(wiek / rok)  # 0.023232822540781017 - wynik float
print(wiek // rok)  # 0 część całkowita z dzielenia (bez zaokrągleń)
print(3 // 2)  # 1
print(wiek % rok)  # modulo, reszta z dzielenia
print(3 % 2)  # 3 //2 = 1 to 2 - 1 = 1 - reszta z dzielenia
print(6 % 2)  # 0 bo 6 // 2 = 3  3 * 2 = 6
print(5 % 2)  # 1
# przy dzieleniu modulo przez 2 (% 2) to mamy albo 0 albo 1
# 10 % 5 -> 0,1,2,3,4
print(wiek ** rok)  # potęgowanie
print(f"{wiek ** rok:,}")
print(74 - 8 * 45 + 8 / 2 + 8 / 2)  # -278.0 - float
print(74 - (8 * 45) + 8 / 2 + 8 / 2)  # -278.0
# ctrl d
print(74 - (8 * 45) + (8 / 2 + 8) / 2)  # -280.0
# ctrl shift - strzałki góra dól - przemieszczanie linijek

# operacje na floatach
print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999
print(0.1 + 0.2)  # 0.30000000000000004
# float jest zapamietywany w pamięci komputera ew sposób wykładniczy
# z tego zapisu wynikaja błedy zaokraglenia
# liczba w postaci a * 2 ^ n
# decimal - zniwelowany problem zaokraglenia - jego wada: powolny
wynik = 0.2 + 0.7
print(f"{wynik:.1f}")  # zaokrąglone przy wypiwsywaniu: 0.9

print(f"Sprawdzenie miennej temp i wiek {temp} {wiek}")  # f- string
# Sprawdzenie miennej temp i wiek 36.6 47
print(f"""
    {wiek}
    {temp}
""")
# "    47
#     36.6"

print(type(4 / 2))  # dzielenie zawsze daje float <class 'float'>

# typ logiczny
# przyjmuje wartości prawda lub fałsz  -> True lub False
czy_znasz_pythona = True
print(czy_znasz_pythona)  # True
print(type(czy_znasz_pythona))  # <class 'bool'> typ logiczny
print(int(czy_znasz_pythona))  # 1 int() - użyte jako rzutowanie typu bool na int
czy_znasz_pythona = False
print(int(czy_znasz_pythona))  # 0

x = 1
print(bool(x))  # True
x = 0
print(bool(x))  # False
x = 100
print(bool(x))  # True
x = -10
print(bool(x))  # True
x = "radek"
print(bool(x))  # True
x = ''  # pusty string
print(bool(x))  # False
x = None  # nic, stan nieokreslony, nie wiem
print(bool(x))  # False

# utworzyłem zmienne i podstawiłem do nich wartości
a = 14
b = 3
print(f"Wynik porówania {a} > {b} = {a > b}")  # Wynik porówania 14 > 3 = True
print("Wynik porównania", a, "<", b, "=", a < b)  # Wynik porównania 14 < 3 = False
print(f"Wynik porówania {a} == {b} = {a == b}")  # == - czy równe,
# Wynik porówania 14 == 3 = False - porównanie a nie podstawienie
print(f"Wynik porówania {a} != {b} = {a != b}")  # != rózne - Wynik porówania 14 != 3 = True
print(f"Wynik porówania {a} >= {b} = {a >= b}")  # Wynik porówania 14 >= 3 = True
print(f"Wynik porówania {a} <= {b} = {a <= b}")  # Wynik porówania 14 <= 3 = False

# and - i
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

# or - lub
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

# not - negacja
print(not True)  # False
print(not False)  # True

my_str = '123456789'
print(my_str.isalnum())  # True
print(my_str.isalpha())  # False - nie sa literami
print(my_str.isdecimal())  # True
print(my_str.isnumeric())  # True
# Wymyslcie kila przykladów stringów i sprawdzcie je wybranymi metodami

print("-----------")
my_str2 = "abcdefghijkl"
print(my_str2.isalnum())
print(my_str2.isalpha())
print(my_str2.isdecimal())
print(my_str2.isnumeric())
print(my_str2.islower())
print(my_str2.isupper())
# True
# True
# False
# False
# True
# False
print("----------")
my_str3 = 'radek12345'
print(my_str3.isalnum())
print(my_str3.isalpha())
print(my_str3.isdecimal())
print(my_str3.isnumeric())
print(my_str3.islower())
print(my_str3.isupper())
# True
# False
# False
# False
# True
# False