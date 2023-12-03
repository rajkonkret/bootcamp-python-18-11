# while - sterowana warunkiem

licznik = 0
while True:  # pętla nieskończona
    print("Komunikat!!!")
    licznik += 1
    if licznik > 10:
        break  # przerwanie bieżacej pętli

print(licznik)  # 11
licznik = 0
while licznik < 10:
    print("Komunikat2!!!!")
    licznik += 1

lista = []
lista_int = []
while True:
    wej = input("Podaj liczbę")  # str()
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista_int.append(int(wej))

print(lista)  # ['4', '5', '6', '7', '8', '9', '1', '2', '3']  lista stringów
print(lista_int)  # [2, 3, 4, 5, 6, 7, 1, 9] - lista intów
