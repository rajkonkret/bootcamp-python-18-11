class Dom:
    """
    klasa opisująca Dom
    """

    # klasa inicjalizujaca
    # metraz, kolor, liczba_okien
    # wyswietl_kolor itd....
    # pola prywatne
    def __init__(self, metraz, kolor, liczba_okien):
        self.__metraz = metraz
        self.__kolor = kolor
        self.__liczba_okien = liczba_okien

    def wyswietl_okna(self):
        print(f"Mam {self.__liczba_okien} okna/okien")

    def ustaw_kolor(self):
        odp = input("Podaj kolor")
        self.__kolor = odp
        self.wyswietl_kolor()

    def ustaw_metraz(self):
        odp = int(input("Podaj nowy metraż"))
        self.__metraz = odp
        self.wyswietl_metraz()

    def wyswietl_kolor(self):
        print(f"Mam kolor: {self.__kolor}")

    def wyswietl_metraz(self):
        print(f"Mam metraż: {self.__metraz}")

    def zwroc_metraz(self):
        return self.__metraz


dom1 = Dom(200, "Czerwony", 12)
dom1.wyswietl_okna()
dom1.wyswietl_kolor()
dom1.wyswietl_metraz()

dom1.ustaw_kolor()

dom2 = Dom("300", "biały", 16)
dom2.wyswietl_metraz()
# print(dom2.zwroc_metraz() + 20)  # TypeError: can only concatenate str (not "int") to str
dom2.ustaw_metraz()