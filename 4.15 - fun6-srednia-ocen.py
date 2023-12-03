# funkcja, ktora oblicza srednia ocen
# ma przyjac dowolna ilość argumentów
# krotka i worek?
#
def srednia(name=None, *cyfry):
    print(cyfry)
    # suma liczb, ilosc liczb
    suma = 0
    try:
        for c in cyfry:
            print(c)
            suma += c
        print(f"Suma wynosi {suma}")
        count = len(cyfry)
        avg = suma / count
    except TypeError:
        print("Błąd typu")
    except ZeroDivisionError:
        print("Nie dzielimy przez zero")
    else:
        print(f"Średnia dla ucznia {name} wynosi {avg}")
    finally:
        print("Zakończyłem działanie")


def srednia2(*cyfry, name=None):
    print(name, cyfry)


srednia()  # () len = 0
srednia(1)  # (1,)
srednia(1, 2, 3)  # (1, 2, 3)
# dodac obsługę błedów try - except
srednia("a", 1, 2)
srednia("Zenek", 3, 4, 5, 2, 1)

srednia2(1, 2, 3, 4, 5, name="Zenek")  # Zenek (1, 2, 3, 4, 5)
srednia2(1, 2, 3, 4, 5, "Zenek")  # None (1, 2, 3, 4, 5, 'Zenek')
# 14:15
