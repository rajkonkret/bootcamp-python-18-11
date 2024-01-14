# pickle - do serializacji i deserializacji danych
# łatwiejsze posługiwwanie sie obiektami np przy zapisywaniu do pliku

import pickle

lista = [1, 2, 3, 4, 5]
print(type(lista))
# zapisac liste do pliku txt
# odczytac liste z pliku

with open("lista.txt", 'w') as f:
    f.write(str(lista))

with open('lista.txt', 'r') as fh:
    lines = fh.read()

print(lines)  # [1, 2, 3, 4, 5]
print(type(lines))  # <class 'str'>
print(lines[0])  # [
l = []
l.extend(lines)
print(l)
# ['[', '1', ',', ' ', '2', ',', ' ', '3', ',', ' ', '4', ',', ' ', '5', ']']
print(list(lines))  # ['[', '1', ',', ' ', '2', ',', ' ', '3', ',', ' ', '4', ',', ' ', '5', ']']

with open('lista.pickle', 'wb') as f:  # wb - pickle wymaga zapisu bajtowego
    pickle.dump(lista, f)  # zapis listy do pliku w bosatci bajtowej

with open('lista.pickle', 'rb') as fh:
    p = pickle.load(fh)  # odczyt listy z bajtów

print(p)  # [1, 2, 3, 4, 5]
print(type(p))  # <class 'list'>
print(p[0])  # 1

lista_ser = pickle.dumps(lista)
print(lista_ser)
# b'\x80\x04\x95\x0f\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03K\x04K\x05e.'

print(pickle.loads(lista_ser))  # [1, 2, 3, 4, 5]
