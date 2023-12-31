# funkcja lambda
# skrocony zapis funkcji
# lambda argumenty: wyrazenie
# lambda ma return - zwraca wynik
# moze byc zdefiniowana w miejscu użycia
import operator

odejmij = lambda a, b: a - b
print(odejmij(6, 8))
print(odejmij(b=8, a=7))

addition = lambda a, b: a + b
print(addition(6, 7))
res = addition(7, 8)
print(f"Wynik dodawania {res}")  # Wynik dodawania 15

res = lambda *args: sum(args)
# sum() - sumowanie elementów
print(res(10, 20))  # 30
print(res(10, 20, 30))  # 60

res = lambda **kwargs: sum(kwargs.values())
print(res(a=10, b=20))  # 30

product = lambda a, b: a * b
print(product(4, 5))  # 20


def product1(nums):
    total = 1
    for i in nums:
        total *= i
    return total


res1 = lambda **kwargs: product1(kwargs.values())
print(res1(a=10, b=30))  # 300


# 8:50

def my_func(n):
    return lambda a: a + n


add10 = my_func(10)
add20 = my_func(20)
add30 = my_func(30)

print(add10(5))  # 15
print(add20(5))  # 25
print(add30(5))  # 35

oblicz_vat = lambda cena, vat=8: cena * (100 + vat) / 100
print(oblicz_vat(1000))
print(oblicz_vat(1000, 23))
print(oblicz_vat(vat=15, cena=1000))
# 1080.0
# 1230.0
# 1150.0

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))  # dziecko
print(wiek(10))  # nastolatek
print(wiek(15))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(25))  # dorosły

# map() - pobiera elemnt, zmienia wg zadanej funkcji
lista = [1, 12, 23, 34, 50, 61, 72, 10, 25, 100]
lista.sort()
print(lista)  # [1, 10, 12, 23, 25, 34, 50, 61, 72, 100]


def zmien(x):
    return x * 2


# pomnożyc każdy element listy przez 2
l = []
l2 = []
for i in lista:
    l.append(i * 2)
    l2.append(zmien(i))
print(l)

print([i * 2 for i in lista])  # [2, 20, 24, 46, 50, 68, 100, 122, 144, 200]
print(lista * 2)  # [1, 10, 12, 23, 25, 34, 50, 61, 72, 100, 1, 10, 12, 23, 25, 34, 50, 61, 72, 100]

print(f"Zastosowanie map: {(map(zmien, lista))}")
# Zastosowanie map: <map object at 0x104853ee0>
print(f"Zastosowanie map: {list(map(zmien, lista))}")
# Zastosowanie map: [2, 20, 24, 46, 50, 68, 100, 122, 144, 200]
print(f"Zastosowanie map: {tuple(map(zmien, lista))}")
# Zastosowanie map: (2, 20, 24, 46, 50, 68, 100, 122, 144, 200)
name = "Radek"
print(list(name))  # ['R', 'a', 'd', 'e', 'k']
# definicja lambdy w miejscu wykonania (funkcja anonimowa)
print(f"Zastosowanie map: {list(map(lambda x: x * 2, lista))}")
# Zastosowanie map: [2, 20, 24, 46, 50, 68, 100, 122, 144, 200]
# for -> map
# def -> lambda
#
# l2 = []
# for i in lista:
#     l2.append(zmien(i))
# def zmien(x):
#     return x * 2

# filter() - filtruje dane wg zadanej funkcji
l_f = []


def filtruj(x):
    if x % 2 == 0:
        return True


for i in lista:
    if filtruj(i):
        l_f.append(i)

print(l_f)  # [10, 12, 34, 50, 72, 100]
# wypisac x < 3
print(f"Zastosowanie filter: {list(filter(lambda x: x < 3, lista))}")
# Zastosowanie filter: [1]
print(f"Zastosowanie filter: {list(filter(lambda x: x > 8, lista))}")
# Zastosowanie filter: [10, 12, 23, 25, 34, 50, 61, 72, 100]
# x > 3 i x < 40
print(f"Zastosowanie filter: {list(filter(lambda x: x > 3 and x < 40, lista))}")
print(f"Zastosowanie filter: {list(filter(lambda x: 3 < x < 40, lista))}")
# Zastosowanie filter: [10, 12, 23, 25, 34]
# Zastosowanie filter: [10, 12, 23, 25, 34]
print(f"Filter: {list(filter(lambda x: x % 2 == 0, lista))}")
# Filter: [10, 12, 34, 50, 72, 100]
print(f"Filter: {list(filter(lambda x: x != 23, lista))}")
# Filter: [1, 10, 12, 25, 34, 50, 61, 72, 100]

list2 = ['one', 'TWO', 'three', 'FOUR']
print(f"Filter: {list(filter(lambda x: x.isupper(), list2))}")
print(f"Filter: {list(filter(lambda x: x.islower(), list2))}")
# Filter: ['TWO', 'FOUR']
# Filter: ['one', 'three']

list3 = ['one', 'two2', 'three3', '88', '99', '102']
numeric = list(filter(lambda x: x.isnumeric(), list3))
print(f"Numeric: {numeric}")  # Numeric: ['88', '99', '102']

alpha = list(filter(lambda x: x.isalpha(), list3))
print(f"Alpha: {alpha}")  # Alpha: ['one']

alphanum = list(filter(lambda x: x.isalnum(), list3))
print(f"Alphanumeric: {alphanum}")  # Alphanumeric: ['one', 'two2', 'three3', '88', '99', '102']

mix = list(filter(lambda x: not x.isnumeric() and not x.isalpha(), list3))
print(f"Mix: {mix}")  # Mix: ['two2', 'three3']

# map()
# list = [1,2,3] -> map(lambda x: x * 2, list) -> [2,4,6]
# list = [1,2,3] -> filter(lambda x: x % 2==0, list) -> [2] - parzyste
# reduce - bierze kolejne elemnty, wykonuje na nich działanie,
# w kolejnym kroku bierze wynik poprzedniego działania, kolejny elemnt
# na tym wykonuje wskazane działanie - podobne do funkcji rekurencyjnej
# list = [1,2,3] -> reduce(lambda a, b: a + b, list) -> 6
# wyn = 1 + 2 = 3
# wyn = 3 + 3 (kolejny element z listy) = 6
from functools import reduce


def add(a, b):
    return a + b


sum_all = reduce(add, [1, 2, 3])
print(f"Reduce [sum_all]: {sum_all}")  # Reduce [sum_all]: 6
# 10:30 - czy nie mielismy miec 15 minut pierwsza?

sum_all = reduce(lambda a, b: a + b, [1, 2, 3])
print(f"Reduce [sum_all]: {sum_all}")  # Reduce [sum_all]: 6
# [2, 20, 24, 46, 50, 68, 100, 122, 144, 200]
sum_all = reduce(lambda a, b: a + b, list(map(lambda n: n * 2, list(filter(lambda n: n % 2 == 0, lista)))))
print(f"Reduce [sum_all]: {sum_all}")  # Reduce [sum_all]: 556

l_1 = [i for i in lista if i % 2 == 0]
print(l_1)  # [10, 12, 34, 50, 72, 100]
l_2 = [i * 2 for i in l_1]
print(l_2)  # [20, 24, 68, 100, 144, 200]
sum_all_2 = reduce(lambda a, b: a + b, l_2)
print(sum_all_2)  # 556

product = reduce(operator.mul, l_2)
print(f"mul: {product}")  # mul: 94003200000
add = reduce(operator.add, l_2)
print(f"add: {add}")  # add: 556

concat_str = reduce(operator.add, ['Python', 'Rocks'])
print(f"Concat:{concat_str}")  # Concat:PythonRocks

min_num = reduce(lambda a, b: a if a < b else b, l_2)
print(f"Min num: {min_num}")  # Min num: 20

print(reduce(lambda a, b: bool(a and b), [0, 0, 1, 0, 0]))  # False
print(reduce(lambda a, b: bool(a and b), [0, 0, 0, 0, 0]))  # False
print(reduce(lambda a, b: bool(a or b), [0, 0, 0, 0, 0]))  # False
print(reduce(lambda a, b: bool(a or b), [0, 0, 1, 0, 0]))  # True
