import time
import numpy as np


# pip install numpy
# numpy - obliczenia na tablicach
# wketoryzacja obliczeń

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Czas wykonania funkcji {func.__name__}: {execution_time}")
        return result

    return wrapper


@measure_time
def my_function():
    pass


@measure_time
def my_wait():
    time.sleep(2)


@measure_time
def my_for_sum():
    suma = 0
    for i in range(15_000_000):
        suma += i
    print("Sum is", suma)


@measure_time
def my_sum_without_for():
    total = sum(range(15_000_000))
    print("Sum is", total)


@measure_time
def my_sum_np():
    total = np.sum(np.arange(15_000_000), dtype=np.int64)
    print("Sum is:", total)


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100, 200, 300, 400, 500, 600, 700, 800, 900]
lista2 = list(range(1_000_000))


@measure_time
def my_for_without_map():
    l = []
    for x in range(1):
        for i in lista2:
            l.append(i * 2)

    # print("Lista is: ", l)


@measure_time
def my_for_with_map():
    l_map = []
    for x in range(1):
        l_map = list(map(lambda x: x * 2, lista2))
    # print("Lista is: ", l_map)


print("------sum-------")
my_function()  # Czas wykonania funkcji my_function: 9.5367431640625e-07
my_wait()  # Czas wykonania funkcji my_wait: 2.0054750442504883
my_for_sum()  # Czas wykonania funkcji my_for_sum: 0.40583181381225586
my_sum_without_for()  # Czas wykonania funkcji my_sum_without_for: 0.1253681182861328
my_sum_np()  # Czas wykonania funkcji my_sum_np: 0.05966472625732422

print("-------map-------")
my_for_without_map()  # Czas wykonania funkcji my_for_without_map: 0.0461421012878418
my_for_with_map()  # Czas wykonania funkcji my_for_with_map: 0.038469791412353516
