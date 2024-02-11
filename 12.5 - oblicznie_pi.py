import random
import time
import threading
import multiprocessing
from concurrent.futures import ThreadPoolExecutor

import numpy as np

total_points_inside_circle = 0


# oblicznie pi metoda monte-carlo
def monte_carlo_pi(num_samples):
    # Losowanie punktów x i y z rozkładu jednostajnego
    x = np.random.uniform(-1, 1, num_samples)
    y = np.random.uniform(-1, 1, num_samples)

    # Sprawdzanie, czy punkty są wewnątrz koła
    inside_circle = x ** 2 + y ** 2 <= 1

    # Obliczenie liczby punktów wewnątrz koła
    num_inside_circle = np.sum(inside_circle)

    # Obliczenie przybliżenia liczby π
    pi_estimate = 4 * num_inside_circle / num_samples

    return pi_estimate


# def monte_carlo_pi(n):
#     points_inside_circle = 0
#
#     for _ in range(n):
#         x = random.uniform(-1, 1)
#         y = random.uniform(-1, 1)
#
#         if x ** 2 + y ** 2 <= 1:
#             points_inside_circle += 1
#
#     return 4 * (points_inside_circle / n)


def no_threads(iterations):
    start = time.time()
    pi = monte_carlo_pi(iterations)
    end = time.time()
    print(f"Bez wątków: {pi}, czas: {end - start}")


def with_threads(iterations):
    num_threads = 8
    iterations_per_thread = iterations // num_threads
    threads = []

    def thread_monte_carlo_pi():
        global total_points_inside_circle
        points_inside_circle_2 = monte_carlo_pi(iterations_per_thread)
        with lock:
            total_points_inside_circle += points_inside_circle_2

    lock = threading.Lock()
    start = time.time()
    for _ in range(num_threads):
        thread = threading.Thread(target=thread_monte_carlo_pi)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    pi = 4 * (total_points_inside_circle / num_threads * 4)
    end = time.time()
    print(f"Z wątkami: {pi}, czas: {end - start}")


# multiprocesy
def with_processes(iterations):
    num_processes = 8
    iterations_per_process = iterations // num_processes

    start = time.time()
    with multiprocessing.Pool(num_processes) as pool:
        results = pool.map(monte_carlo_pi, [iterations_per_process] * num_processes)
        pi = sum(results) / num_processes
        end = time.time()
        print(f"Z procesami: {pi}, czas: {end - start}")


# ThreadPoolExector
def with_thread_pool_executor(iterations):
    num_threads = 8
    iterations_per_thread = iterations // num_threads

    start = time.time()
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = list(executor.map(monte_carlo_pi, [iterations_per_thread] * num_threads))
        pi = sum(results) / num_threads
    end = time.time()
    print(f"ThreadPoolExecutor: {pi}, czas: {end - start}")


# iterations = 10_000_000
iterations = 100_000_000

if __name__ == '__main__':
    no_threads(iterations)
    with_threads(iterations)
    with_processes(iterations)
    with_thread_pool_executor(iterations)
