# napisać dekorator, który zamieni małe litery na duże
# zakładamy, że funkcją, która dekorujemy zwraca stringa

def uppercase_decorator(function):
    def wrapper():
        result = function()
        return result.upper()

    return wrapper


def bold_decorator(func):
    def wrapper():
        result = func()
        return f"\033[1m" + result + "\033[0m"

    return wrapper


@uppercase_decorator
def greeting():
    return "Hello World!"


@bold_decorator
@uppercase_decorator
def greeting2():
    return "Hello World!"


print(greeting())  # HELLO WORLD!
print(greeting2())  # HELLO WORLD!
# 13:00
