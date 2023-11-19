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

