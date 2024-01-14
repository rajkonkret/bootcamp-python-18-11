# tworzenie wyjątku
class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


# print(2 / 0)  # ZeroDivisionError: division by zero
# raise ZeroDivisionError("Nie dziel przez zero")  # ZeroDivisionError: Nie dziel przez zero

try:
    x = int(input("Podaj liczbę całkowitą"))
    if x < 0:
        print("Liczba ma być większa od zera")
        raise MyException("Liczba musi byc dodatnia")  # raise - rzucic, wywołac wyjatek
    # Traceback (most recent call last):
    #   File "/Users/radoslawjaniak/PycharmProjects/bootcamp-python-18-11/8.9 - kl18a - exception.py", line 12, in <module>
    #     raise MyException("Liczba musi byc dodatnia")
    # MyException: Liczba musi byc dodatnia
except MyException:
    print("Wystąpił wyjątek MyException")
except ValueError:
    print("Wystapił bład wartości")
except TypeError:
    print("Bład typu")
except Exception as e:
    print("Bład", e)
else:
    print("Wprowadziłeś poprawną wartość")
finally:
    print("Zakończone działanie")
