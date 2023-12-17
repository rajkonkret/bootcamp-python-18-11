class Human:
    """
    Klasa Human opisująca człowieka w pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec='k'):
        """
            Metoda inicjalizująca klasy (konstruktor)

        :param imie: przechowuje str imie
        :param wiek:
        :param wzrost:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        """
        metoda witająca
        :return:
        """
        print(f"Nazywam się {self.imie}")

    # metoda do odczytu wieku
    def podaj_wiek(self):
        print("Mam", self.wiek, "lat")

    def podaj_wzrost(self):
        print(f"Mam {self.wzrost} cm")

    def ruszaj(self):
        if self.plec == 'm':
            print("Ruszyłem w drogę")
        else:
            print("Ruszyłam w drogę")


cz1 = Human('Anna', 27, 170)
print(cz1)  # <__main__.Human object at 0x104275f90>
print(cz1.imie)  # Anna
print(cz1.__doc__)
print(cz1.__init__.__doc__)  # dokumentacja metody __init__
cz1.powitanie()
cz1.podaj_wzrost()
cz1.ruszaj()  # Ruszyłam w drogę

cz2 = Human('Radek', 46, 190, "m")
cz2.podaj_wzrost()
cz2.powitanie()
# Mam 190 cm
# Nazywam się Radek
cz2.ruszaj()  # Ruszyłem w drogę
