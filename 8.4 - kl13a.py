class Matematyka:

    @staticmethod
    def dodaj(a, b):
        return a + b

    @staticmethod
    def odejmij(a, b):
        return a - b


wynik = Matematyka.dodaj(5, 6)
print(wynik)  # 11
print(Matematyka.odejmij(9, 7))  # 2


# klase z metodami statycznymi
# celcjusz na fahrenhaity
# frenheit na celcjusz

class KalkulatorTemperatur:
    @staticmethod
    def celcius_na_fahrenheit(celcius):
        return celcius * 9 / 5 + 32

    @staticmethod
    def fahrenheit_na_celcius(fahrenheit):
        return (fahrenheit - 32) * 5 / 9


print(KalkulatorTemperatur.fahrenheit_na_celcius(100))  # 37.77777777777778
print(KalkulatorTemperatur.celcius_na_fahrenheit(2))  # 35.6
