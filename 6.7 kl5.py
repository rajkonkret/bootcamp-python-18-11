# dziedziczenie
class Pojazd:
    def __init__(self, kolor):
        self.kolor = kolor

    def info(self):
        print(f"Kolor: {self.kolor}")


class Samochod(Pojazd):  # dziedziczy po klasie pojazd
    """
    Samochód
    """

    def __init__(self, kolor, marka="Fiat"):
        super().__init__(kolor)  # super() - uzycie z klasy nadrzędnej
        self.marka = marka

    def info(self):
        super().info()  # wywołanie metody info() z klasy nadrzędnej
        print(f"Marka: {self.marka}")


class Rower(Pojazd):
    """
    klasa rower
    """

    def info(self):
        pass


class Rower2(Samochod):
    """
    Rower dziedziczy po samochodzie
    """


poj = Pojazd("Czerwony")
poj.info()  # Kolor: Czerwony

car = Samochod("Biały")
print(car.kolor)
car.info()  # Kolor: Biały
# Kolor: Biały
# Marka: Fiat
rower = Rower("Zólty")
rower2 = Rower2("Zielony")

lista = [poj, car, rower, rower2]
print(lista)
# [<__main__.Pojazd object at 0x100b92c10>,
# <__main__.Samochod object at 0x100b92d50>,
#  <__main__.Rower object at 0x100cb2fd0>]


print(type(car))
print(type(poj))
# <class '__main__.Samochod'>
# <class '__main__.Pojazd'>
# Obiekty różnego typu, ale dzięki dziedziczeniu i zasadom polimorfizmu
# udaję sie na nich wykonać wspólna operacje
# info()
# polimorfizm
for i in lista:
    print(i.__class__.__name__)
    i.info()

# Kolor: Czerwony
# Biały
# Kolor: Biały
# Marka: Fiat
# [<__main__.Pojazd object at 0x10304a110>,
# <__main__.Samochod object at 0x10304ac10>]
# <class '__main__.Samochod'>
# <class '__main__.Pojazd'>
# Kolor: Czerwony
# Kolor: Biały
# Marka: Fiat
