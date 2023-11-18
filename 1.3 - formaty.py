user = "Tomek"  # str
wiek = 39  # int
wersja = 3.90001  # float - zmiennoprzecinkowe
liczba = 123456712456  # int (Python nie ma typów w rodzaju bigint czy double, longint etc...)

print("Witaj %s masz teraz %d lat" % (user, wiek))  # Witaj Tomek masz tera 39 lat
# przy formatowaniu z %, python spradza typy
# print("Witaj %d masz teraz %s lat" % (user, wiek))  # TypeError: %d format: a real number is required, not str
# %s - string
# %d - digit
print("Witaj %(user)s, masz teraz %(wiek)d lat" % {'user': user, 'wiek': wiek})
# Witaj Tomek, masz teraz 39 lat
print("Witaj %(user)s, masz teraz %(age)d lat" % {'user': user, 'age': wiek})
# Witaj Tomek, masz teraz 39 lat

# zrobcie podobny tekst z uzyciem f-string i format()
# tu typy nie są sprawdzane
print(f"Witaj {user}, masz teraz {wiek}")  # obecnie podstawowy sposób wyswietlania
print("Witaj {}, masz teraz {} lat".format(user, wiek))
print("Witaj {}, masz teraz {} lat".format(wiek, user))
# Witaj Tomek, masz teraz 39 lat
# Witaj 39, masz teraz Tomek lat

print("Używamy wersji Python %i" % 3)  # Używamy wersji Python 3
print("Używamy wersji Python %f" % 3.9)  # Używamy wersji Python 3.900000
print("Używamy wersji Python %.1f" % 3.9)  # .1f - jedna cyfra po przecinku, Używamy wersji Python 3.9
print("Używamy wersji Python %.2f" % 3.9)  # .2f - dwie cyfry po przecinku, Używamy wersji Python 3.90
print("Używamy wersji Python %.f" % 3.9)  # .f - wypisanie z 0 liczb po przecinku,
# to oznacza zaokrąglenie przy wypisywaniu, Używamy wersji Python 4
print("Używamy wersji Python %.0f" % 3.9)  # Używamy wersji Python 4

print("Używamy wersji Pythona {}".format(wersja))  # Używamy wersji Pythona 3.90001
print(f"Używamy wersji Pythona {wersja}")  # Używamy wersji Pythona 3.90001
print(f"Używamy wersji Pythona {wersja:.1f}")  # Używamy wersji Pythona 3.9
print(f"Używamy wersji Pythona {wersja:.2f}")  # Używamy wersji Pythona 3.90
print(f"Używamy wersji Pythona {wersja:.0f}")  # Używamy wersji Pythona 4
# przy string format musimy jawnie pokaza ilosc miejsc po przecinku,
# Dla 0 miejsc po przecinku musi byc .0f

# spróbujcie wypisac tą duża liczbe
print(liczba)  # 123456712456
print("Nasza duża liczba {}".format(liczba))  # Nasza duża liczba 123456712456
print("Nasza duża liczba {:,}".format(liczba))  # Nasza duża liczba 123,456,712,456
print(f"Nasza duża liczba {liczba:,}")  # Nasza duża liczba 123,456,712,456
# zamienic przy wyppisawaniu tej liczby , na ., , na spację
print(f"Nasza duża liczba {liczba:,}".replace(",", "."))
print(f"Nasza duża liczba {liczba:,}".replace(",", " "))
# Nasza duża liczba 123.456.712.456
# Nasza duża liczba 123 456 712 456
liczba_human_re = f"Nasza duża liczba {liczba:,}".replace(",", " ")
print(liczba_human_re)  # Nasza duża liczba 123 456 712 456
liczba2 = 123_456_789_567
print(liczba2)
print(type(liczba2))
# 123456789567
# <class 'int'>

print(f"{user:>10}")  # "     Tomek" - wyrównał do prawej
print(f"{user:<20}")  # "Tomek        " - wyrównal do lewej
print(f"{user:^25}")  # "          Tomek          " - wycentrował
