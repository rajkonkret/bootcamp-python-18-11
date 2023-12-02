import random

# do działąnia na liczbach pseudolosowych

print(random.randint(1, 6))  # 1..6 int
print(random.random())  # 0.6697487156379939 float 0.....0.999999
print(random.random() * 10)  # 5.656179257376845 float -> 0...99999
print(random.randrange(6))  # int 0..5
print(random.randrange(1, 6))  # int 1..5

lista = [5, 7, 45, 34, 56]
print(random.choice(lista))  # 45

print("----------------------------")
# maszyna lotto
lista_lotto = list(range(1, 50))  # lista liczb od 1 do 49
# print(lista_lotto)
liczby_wylosowane = []
# print(random.choice(lista_lotto))
# print(random.choice(lista_lotto))
# print(random.choice(lista_lotto))
# print(random.choice(lista_lotto))
# print(random.choice(lista_lotto))
# print(random.choice(lista_lotto))
wyn = random.choice(lista_lotto)
lista_lotto.remove(wyn)
print(wyn)
liczby_wylosowane.append(wyn)
wyn = random.choice(lista_lotto)
lista_lotto.remove(wyn)
print(wyn)
liczby_wylosowane.append(wyn)
wyn = random.choice(lista_lotto)
lista_lotto.remove(wyn)
print(wyn)
liczby_wylosowane.append(wyn)
wyn = random.choice(lista_lotto)
lista_lotto.remove(wyn)
print(wyn)
liczby_wylosowane.append(wyn)
wyn = random.choice(lista_lotto)
lista_lotto.remove(wyn)
print(wyn)
liczby_wylosowane.append(wyn)
wyn = random.choice(lista_lotto)
lista_lotto.remove(wyn)
print(wyn)
liczby_wylosowane.append(wyn)

print(f"Lista wylosowanych {liczby_wylosowane}")

print(random.choices(lista_lotto, k=6))  # losowanie sześciu powtarzających się [16, 5, 22, 10, 33, 10]
print(random.sample(lista_lotto, 6))  # losowanie niepowtarzajacych się liczb [43, 4, 1, 48, 42, 45]
print(random.sample(lista_lotto, k=6))  # losowanie niepowtarzajacych się liczb [12, 27, 11, 22, 25, 40]
