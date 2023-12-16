def sub_decorator(func):
    def wrapper(num1, num2):
        if num1 < num2:
            num1, num2 = num2, num1  # zamienia miejscami
            return func(num1, num2)

    return wrapper


@sub_decorator
def substract(num1, num2):
    res = num1 - num2
    print("Result is:", res)


substract(2, 4)  # Result is: 2
# zamiana zmiennych miejscami
a, b = 1, 2
print(b)
a, b = b, a
print(b)
