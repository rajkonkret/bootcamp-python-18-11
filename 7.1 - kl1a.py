import math  # biblioteka do działań matematycznych


class MyFirstClass:
    """
    Klasa w Pythonie, opisująca punkty w przestrzeni x i y
    """

    def __init__(self, x=0, y=0):
        """
        funkcja inicjalizująca
        :param x:
        :param y:
        """
        # self.x = x
        # self.y = y
        # Po dodaniu funkcji move()
        self.move(x, y)  # wywołanie funkcji move()

    def move(self, x: float, y: float) -> None:
        """
        funkcja przesuwa punkt w dane miejsce
        :param x:
        :param y:
        :return: None
        """
        self.x = x
        self.y = y

    def reset(self) -> None:
        """
        funkcja wraca punkt do miejsca 0,0
        :return: None
        """
        self.move(0, 0)

    def calculate(self, other: "MyFirstClass") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)

    # funkcja odpowiada za sposob w jaki jest wyswietlany obiekt
    def __str__(self):
        return f"({self.x, self.y})"

    # reprezentacja obiektu
    def __repr__(self):
        return f"Point({self.x, self.y})"


ob = MyFirstClass()  # <__main__.MyFirstClass object at 0x104666590>
# po dodaniu funkcji __str__ opis wygląda tak: ((0, 0))
print(ob)
print(ob.x)
print(ob.y)
ob.move(4, 5)
print(ob)  # ((4, 5))
ob.reset()
print(ob)  # ((0, 0))
ob2 = MyFirstClass(5, 7)
print(ob2)  # ((5, 7))

lista_punkty = [ob, ob2]
print(lista_punkty)  # [<__main__.MyFirstClass object at 0x100716f50>, <__main__.MyFirstClass object at 0x100716f90>]
# po dodaniu __repr__
# [Point((0, 0)), Point((5, 7))]
ob_str = str(ob)  # uzywa __str__
lista2 = [ob_str]
print(lista2)  # ['((0, 0))']
print(ob.calculate(ob2))  # 8.602325267042627
# Używamy hintów (podpowiedzi)
# one nie weryfikuja typu
# ob.calculate("a")  # AttributeError: 'str' object has no attribute 'x'
# stworzyć dwa obiekty i obliczyc odległość miedzy nimi
