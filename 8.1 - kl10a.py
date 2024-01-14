class Pojazd:
    def serwis(self):
        print("Serwisowanie pojazdu")


class SamochodOsobowy(Pojazd):
    def serwis(self):
        print("Serwisowanie samochodu osobowego")


class SamochodDostawczy(Pojazd):
    def serwis(self):
        print("Serwisowanie samochodu dostawczego")


class PojazdSluzbowy(Pojazd):
    def rejestracja_sluzbowa(self):
        print("Rejestracja pojazdu słuzbowego")


class SamochodSluzbowyOsobowy(SamochodOsobowy, PojazdSluzbowy):
    pass


if __name__ == '__main__':
    car1 = SamochodSluzbowyOsobowy()
    car1.serwis()
    car1.rejestracja_sluzbowa()
