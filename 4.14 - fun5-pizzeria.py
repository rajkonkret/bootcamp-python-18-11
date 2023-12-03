# zrobic funkcje zagniezdzoną, ktora zwraca funkcje w zależności od złożonego zamówienia

def restauracja(typ_zamowienia):
    print("Witamy w naszej restauracji")

    def zamow_pizze(skladniki="pieczarki"):
        print("Zamówiona pizza, składniki: ", skladniki)

    def zamow_napoj(nazwa="herbata"):
        print("Zamow napoj", nazwa)

    if typ_zamowienia.lower() == 'pizza':
        return zamow_pizze
    else:
        return zamow_napoj  # zwracam adres funkcji


zamowienie_pizza = restauracja('pizza')
zamowienie_pizza()  # Zamówiona pizza
zamowienie_pizza("pieczarki, szynka")
zamowienie_pizza(["pieczarki", "szynka"])

zamowienie_napoj = restauracja('napoj')
zamowienie_napoj()
# Witamy w naszej restauracji
# Zamow napoj
zamowienie_napoj('cola')
# Witamy w naszej restauracji
# Zamówiona pizza, składniki:  pieczarki
# Zamówiona pizza, składniki:  pieczarki, szynka
# Zamówiona pizza, składniki:  ['pieczarki', 'szynka']
# Witamy w naszej restauracji
# Zamow napoj herbata
# Zamow napoj cola
