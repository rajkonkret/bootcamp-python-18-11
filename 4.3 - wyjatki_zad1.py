# wyjątki

try:
    # print(5 / 0)  # ZeroDivisionError: division by zero
    print("a" / 2)
    print("Radek")
except ZeroDivisionError:
    print("Nie dziel przez zero")
except Exception as e:
    print("Bład", e)  # Bład unsupported operand type(s) for /: 'str' and 'int'
else:
    print("Wykona się tylko gdy błedu nie ma")
finally:
    print("Wykona się niezależnie czy błąd był czy nie")

print("Dalsza część programu")
# Nie dziel przez zero
# Dalsza część programu
