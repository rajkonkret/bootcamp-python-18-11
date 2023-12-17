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


cz1 = Human('Anna', 27, 170)
print(cz1)  # <__main__.Human object at 0x104275f90>
print(cz1.imie)  # Anna
print(cz1.__doc__)
print(cz1.__init__.__doc__)  # dokumentacja metody __init__
cz1.powitanie()
