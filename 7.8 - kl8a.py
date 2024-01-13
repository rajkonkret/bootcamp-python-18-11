# dziedziczenie diamentowe

class A:
    def method(self):
        print("Metoda z klasy A")


class B(A):
    def method(self):
        print("Metoda z klasy B")


class C(A):
    def method(self):
        print("Metoda z klasy C")


class D(B, C):  # kolejnosc ma znaczenie
    pass


# Traceback (most recent call last):
#   File "/Users/radoslawjaniak/PycharmProjects/bootcamp-python-18-11/7.8 - kl8a.py", line 22, in <module>
#     class E(A, D):
# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases A, D
# class E(A, D):
#     pass


class F(D, A):
    pass


d = D()
d.method()  # Metoda z klasy B
print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

# e = E()
# Traceback (most recent call last):
#   File "/Users/radoslawjaniak/PycharmProjects/bootcamp-python-18-11/7.8 - kl8a.py", line 22, in <module>
#     class E(A, D):
# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases A, D

f = F()
f.method()
print(F.__mro__)
# (<class '__main__.F'>, <class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
