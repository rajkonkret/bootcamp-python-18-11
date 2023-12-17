# hermetyzacja, enkapsulacje
class Car:
    """
    Klasa opsiujaca samochód w pythonie
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.__predkosc = 0  # pole zostało oznaczone jako prywatne (hermetyzacja)

    def gaz(self):
        self.__zmien_bieg()
        self.__predkosc += 10

    def licznik(self):  # enkapsulacja
        print(f"Prędkość wynosi {self.__predkosc} km/h")

    def get_predkosc(self):
        return self.__predkosc

    def hamuj(self):
        if self.__predkosc > 0:
            self.__predkosc -= 10
        else:
            self.__predkosc = 0
            print("Zatrzymałeś się")

    def __zmien_bieg(self):  # metoda prywatna
        print("Zmiana biegu")


car1 = Car("Peugeot", 2023)
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
# po oznaczeniu pola jako prywatne
# AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
# print(car1.__predkosc)  # 50
car1.licznik()  # Prędkośc wynosi 50 km/h
# shift tab  - cofniecie tabulacji
# po oznaczeniu pola prywatnego
# to pole jest innym polem niz pole prywatne klasy o tej nazwie
# pole w klasie __predkosc sie nie zmienia
car1.__predkosc = 0  # pole globalne, inna niz prywatna
car1.licznik()  # Prędkość wynosi 50 km/h
print(car1.__predkosc)  # 0 dla pola globalnego ale stan obiektu nie został zmieniony
print(car1.get_predkosc())  # 50
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.licznik()  # Prędkość wynosi 0 km/h
car1.hamuj()  # Zatrzymałeś się
