from abc import ABC, abstractmethod


class Counter(ABC):
    def __init__(self, values=0):
        self.values = values

    def increment(self, by=1):
        self.values += by  # values = values + by

    @abstractmethod
    def drukuj(self):
        pass

    @classmethod  # metoda klasowa, tworzy obiekt klasy z innego obiektu
    def from_counter(cls, counter):
        return cls(counter.values)

    @staticmethod  # metoda statyczna - metoda dla której nie trzeba tworzyc obiektu klasy
    def from_string():
        print("Metoda statyczna")


class NewCounter(Counter):
    """
    Licznik bez metody drukuj
    """


class BoundedCounter(Counter):
    MAX = 100

    def __init__(self, values=0):
        if values > self.MAX:
            raise ValueError(f"Wartość nie może być większa od {self.MAX}")
        super().__init__(values)  # obowiązkowo w konstrukotorze należy wywołać super().__init__()

    def drukuj(self):
        print("Drukuje...", self.values)


# TypeError: Can't instantiate abstract class NewCounter with abstract method drukuj
# nie nadpisalismy metody drukuj()
# nc = NewCounter()

c1 = BoundedCounter()
c1.drukuj()
c1.increment(5)
c1.drukuj()  # Drukuje... 5

# bc2 = BoundedCounter(101)  # ValueError: Wartość nie może być większa od 100

c2 = BoundedCounter(c1.values)
c2.drukuj()  # Drukuje... 5

# z użyciem metody typu classmethod
c3 = c2.from_counter(c2)
c3.drukuj()  # Drukuje... 5

# Uzycie metody statycznej
# nie musimy tworzyc obiektu klasy
# wywołujemy bezposrednio na klasie
Counter.from_string()  # Metoda statyczna
