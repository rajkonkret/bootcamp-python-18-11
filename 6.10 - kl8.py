# metoda/klasa abstrakcyjna
# klasa abstrakcyjna to jest taka klasa, która zawiera metode abstrakcyjna
# nie mozna utworzyc obiektu (instancji) takiej klasy
# obowiązkowo należy nadpisac przy dziedziczeniu wszystkie metody abstrakcyjne z tej klasy
# metoda abstrakcyjna - metoda oznaczona jako @abstractmethod
# nie wykonuje czynności
from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opisujaca ptaka w Pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)

    @abstractmethod  # metoda abstrakcyjna - musimy nadpisac
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    def __init__(self, gatunek):
        super().__init__(gatunek, 0)  # przekazanie szybkosci jako wartosc stała 0

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("Kokoko ko koko")

    def dziobanie(self):
        print("Tu", self.gatunek, 'Idę sobie podziobać')


class Orzel(Ptak):
    """
    Orzel
    """

    # metoda musi byc nadpisana
    # gdy nie nadpiszemy dostaniemy bład
    # TypeError: Can't instantiate abstract class Orzel with abstract method wydaj_odglos
    def wydaj_odglos(self):
        print("kier kiir")

    def poluj(self):
        print("Tu", self.gatunek, "Rozpoczynam polowanie!!!")


# po dodaniu do klasy metody abstrakcyjnej klasa stała sie abstrakcyjna
# # nie mozna stworzy cobiektów klasy Ptak
# # TypeError: Can't instantiate abstract class Ptak with abstract method wydaj_odglos
# or1 = Ptak("Orzel", 40)
# or1.latam()
#
# kur1 = Ptak("Kura", 0)
# kur1.latam()  # Tu Kura Lecę z szybkością 0

kur2 = Kura("Kura")
kur2.latam()  # Tu Kura Ja nie latam
kur2.wydaj_odglos()
kur2.dziobanie()

or2 = Orzel("Orzel", 45)
or2.latam()
or2.wydaj_odglos()
or2.poluj()
