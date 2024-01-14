# iteratory

lista = [1, 2, 3, 4, 5]
for i in lista:
    print(i)
iterator = iter(lista)
print(iterator)
print(type(iterator))  # <class 'list_iterator'>
# for i in iterator:
#     print(i)

print(next(iterator))  # 1
print("Zrób cos")
print(next(iterator))  # 2
print(next(iterator))
print(next(iterator))
print(next(iterator))


# print(next(iterator))  # StopIteration


class Count:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


print("------------")
counter = Count(1, 5)
while True:
    try:
        number = next(counter)
        print(number)
    except StopIteration:
        break

counter2 = Count(1, 20)
print(next(counter2))
print(next(counter2))
print(next(counter2))
### Zalety Używania Iteratorów

# 1. **Zarządzanie Pamięcią**: Iteratory są efektywne pod względem pamięci,
# ponieważ nie wymagają wczytywania całego zbioru danych do pamięci na raz.
# Są one szczególnie użyteczne przy przetwarzaniu dużych zbiorów danych.
#
# 2. **Uniwersalność**: Można je stosować do różnych typów struktur danych,
# ułatwiając pisanie generycznego, wielokrotnego użytku kodu.
#
# 3. **Leniwe Wykonanie**: Iteratory realizują leniwe wykonanie,
# co oznacza, że generują elementy na żądanie, co może być korzystne dla wydajności.
