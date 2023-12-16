# funkcja rekurencyjna
# funkcja, który wywołuja samą siebie

def add(num):
    if num == 0:
        return 0
    else:
        return num + add(num - 1)


# 5 + 4 + 3 + 2 + 1 + 0 = 15

print(add(5))  # 15


def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)


# 5 * 4 * 3 * 2 * 1 = 120  - silnia
print(factorial(5))


def nwd(a, b):
    if b == 0:
        return a
    else:
        return nwd(b, a % b)


print(48 % 18)  # 12
print(18 % 12)  # 6
print(12 % 6)  # 0
print(nwd(48, 18))  # 6


def fibonacci(num):
    if num <= 1:
        return num
    if num == 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


nums = int(input("Podaj zakres"))
for i in range(nums):
    print(fibonacci(i))
