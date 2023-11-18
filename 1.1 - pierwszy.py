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
