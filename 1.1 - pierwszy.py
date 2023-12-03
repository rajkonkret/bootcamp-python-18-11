import sys

# print() - wydrukuj/wypisz
print()  # wyswietlenie pustej lini
print("Nazywam się Radek")  # tekst , który ma być wyświetlony musi być w cudzysłowach
# Nazywam się Radek
print('Nazywam się Radek')
# Nazywam się Radek
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Paulina')
print('Nazywam się Jacek')
print('Nazywam się Tadek')
print('Nazywam się Mateusz')
print('Nazywam się Wojtek')
# ctrl d - powielanie lini w ktorej ustawiliśmy kursor
# ctrl z - cofnij
# type() - sprawdzenie typy jakim jest dana
print(type('Radek'))  # <class 'str'> - string - czyli tekst

print("39" + "14")  # 3914 złączył teksty (konkatenacja)

print(39)  # 39
print(type(39))  # <class 'int'> - liczba calkowita (integer)

# print("39" + 14)  # TypeError: can only concatenate str (not "int") to str
# silne typowanie - sam nie zamienia typów danch
print("39" + str(14))  # str() - zamiana(rzutowanie) na string 3914
print(int("39") + 14)  # 53, int() - rzutowanie na integer

print(5 * "4")  # 44444 - konkatenacja (wielokrotna)
print(sys.int_info)  # wyswietlenie informacji o int
# sys.int_info(bits_per_digit=30, sizeof_digit=4)
# 13:45

# zmienna - pudełko na dane (przechowywane w pamięci)
# typowanie dynamiczne - typ zmiennej jest określany na podstwie typu danej do niej wrzuconej
# zmienna definiujemy poprzez nadanie jej nazyi wrzucenie danej do niej
# snake_case - konwencja nazewniczna stosowana dla nazw zmiennych
# camelCase, PascalCase, kebab-case - inne podtsawowe konwencje nazewnicze

name = "Radek"  # zapisanie danych do zmiennej
print(type(name))  # <class 'str'>
# name_info: str - zmienna z podpowiedią typu, nie jest to walidacja typu
name_info: str = "Maciek"
print(type(name_info))  # <class 'str'>
# wypisanie zawartości zmiennej (nazwa zmiennej bez cudzysłowia)
print(name)  # Radek
print(name_info)  # Maciek
# Sprawdźmy czy rzeczywiscie str oznaczy tylko podpowiedź
name_info = 50  # wrzucamy liczbę int
print(name_info)  # pomimo wrzucenia int program nadal działa 50
print(type(name_info))  # <class 'int'>

age = 48
print(age)  # 48
print(type(age))  # <class 'int'>
age = "Radek"

# print(age + name_info)  # TypeError: can only concatenate str (not "int") to str
# print(int(age) + name_info)  # ValueError: invalid literal for int() with base 10: 'Radek'
age = "48"
print(int(age) + name_info)  # 98

age2 = "zmiana pliku"
