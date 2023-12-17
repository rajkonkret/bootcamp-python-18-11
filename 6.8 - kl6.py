class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja

    def przedstaw_sie(self):
        print(f"Cześć, jestem {self.imie} {self.nazwisko}")

    def oblicz_pensje(self):
        return self.pensja


# klasa Manadzer, ktora ndpisze klase Pracownik
# zastanówcie sie co dziedziczyc, co nadpisać
class Manager(Pracownik):
    """
    klasa Manager
    """

    def __init__(self, imie, nazwisko, pensja, premia):
        super().__init__(imie, nazwisko, pensja)
        self.premia = premia

    def oblicz_pensje(self):
        return int(self.premia) + int(self.pensja)


pracownik = Pracownik("Jan", "Kowalski", 5000)
pracownik.przedstaw_sie()
wyn_prac = pracownik.oblicz_pensje()
print(f"Wynagrodzenie dla pracownika {pracownik.imie} {pracownik.nazwisko}: {wyn_prac}")

# manago = Manager("Zofia", "Madej", 10000, 10000)
manago = Manager(nazwisko="Zofia", imie="Madej", pensja=10000, premia=10000)
manago.przedstaw_sie()
wyn_manago = manago.oblicz_pensje()
print(f"Wynagrodzenie dla managera {manago.imie} {manago.nazwisko}: {wyn_manago}")
# Cześć, jestem Jan Kowalski
# Wynagrodzenie dla pracownika Jan Kowalski: 5000
# Cześć, jestem Zofia Madej
# Wynagrodzenie dla managera Zofia Madej: 20000
