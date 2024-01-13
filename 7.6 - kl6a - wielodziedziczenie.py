# wielodziedziczenie - dziedziczenie po kilku klasach
# dziedziczenie mieszane

class A:
    def method(self):
        print("Metoda klasy A")


class B:
    def method(self):
        print("Metoda klasy B")


# dziedziczenie mieszane
class C(B, A):  # kolejnosc ma znaczenie
    # (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
    """
    Klasa dziedziczy po klasie B i A
    """


class D(A, B):
    """
    Klasa dziedziczy po A i B
    """


class E(A, B):
    def method(self):
        print("Metoda z klasy E")


class F(B, A):
    """
    Metoda dziedziczy po klasie B i A
    """

    def method(self):
        A.method(self)  # jawne wskazanie z której klasy uzyjemy methody


class G(A, B):
    """
    Dziedziczy po A i B
    """

    def method(self):
        super().method()  # super() uzycie z klasy wyzszej, uzycie metody method()
        print("Dopisane")


a = A()
a.method()  # Metoda klasy A

b = B()
b.method()  # Metoda kalsy B

c = C()
c.method()  # Metoda kalsy B
print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

d = D()
d.method()  # Metoda klasy A
print(D.__mro__)  # (<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

e = E()
e.method()  # Metoda z klasy E

f = F()
f.method()  # Metoda klasy A

g = G()
g.method()
# Metoda klasy A
# Dopisane
print(G.__mro__)
# (<class '__main__.G'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
