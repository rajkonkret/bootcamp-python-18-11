dictionary = {'imie': "Radek", 'nazwisko': "Kowalski"}
print(dictionary)
print(type(dictionary))

print(dictionary.keys())
# dict_keys(['imie', 'nazwisko'])


# wyswietli klucze
for k in dictionary:
    print(k)

for k in dictionary.keys():
    print(k)

# wyswietlenie eartości
for value in dictionary.values():
    print(value)

# wyswietlenie par(elemntów)
for k, v in dictionary.items():
    print(k, "=>", v)  # nazwisko => Kowalski
