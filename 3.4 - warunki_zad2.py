# # 3.10 - match case
#
# lista = []
# lang = input("Podaj znany Ci język programowania")
#
# match lang.lower().replace(" ", ""):
#     case "python":
#         print("Lubię pythona")
#         lista.append(lang)
#     case "java":
#         print("Java to kawa")
#         lista.append(lang)
#     case "c++":
#         print("Kto to jeszcze uzywa")
#         lista.append(lang)
#     case _:  # wartość domyślna
#         print("Nie znam takiego języka")
#
# print(f"Lista odpowiedzi {lista}")
# dane = [1, 2, 3]
dane = {"nazwa": "radek", "wiek": 67}
match dane:
    case [a, b, c]:
        print(f"Lista z trzema elementami {a} {b} {c}")
    case {"nazwa": n, "wiek": w}:
        print(f"Słownik reprezentujący osobę {n}, wiek {w}")
    case _:
        print("Inny typ danych")
# Lista z trzema elementami 1 2 3
# Słownik reprezentujący osobę radek, wiek 67
