# klasa - szablon, wzór wg którego budujemy obiekty
# wykorzystywana w programowniu obiektowym
# enkapsulacja, hermetyzacja, abstrakcja,dziedziczenie i polimorfizm
# obiekt - instancja klasy - nadane ma cechy wg szablonu
# pola, funkcje

class Human:
    """
    Klasa Human opisująca człowieka w Pythonie
    """
    imie = ""
    wiek = "None"
    plec = 'k'

    def powitanie(self):
        print(f"Nazywam się {self.imie}")

    # metoda do odczytu wieku
    def podaj_wiek(self):
        print("Mam", self.wiek, "lat")


class X:
    pass


cz1 = Human()  # tworzenie obiektu
# komentarz wielolinijkowy służy jako dokumentacja kodu
print(cz1.__doc__)  # Klasa Human opisująca człowieka w Pythonie
print(print.__doc__)
# sep
#     string inserted between values, default a space.
#   end
#     string appended after the last value, default a newline.
#   file
#     a file-like object (stream); defaults to the current sys.stdout.
#   flush
#     whether to forcibly flush the stream.
print(X.__doc__)  # None
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
# "
# None
# k"
cz1.imie = "Anna"
print(cz1.imie)  # Anna
cz1.wiek = 27
print(cz1.wiek)  # 27
print(cz1.plec)  # k
cz1.powitanie()

# stworzyc obiekt odmiennej płci
# nadac imie, wiek, plec
cz2 = Human()
cz2.imie = "Radek"
cz2.wiek = 58
cz2.plec = 'm'
print(cz2.imie)
print(cz2.wiek)
print(cz2.plec)
cz2.powitanie()  # Nazywam się Radek
cz2.podaj_wiek()
