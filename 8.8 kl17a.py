# stworzyc słownik
# zapisac słownik do pliku za pomoca pickle
# odczytac za pomoca pickle
import pickle

slownik = {"klucz1": "wartosc1", "klucz2": "wartosc2"}

with open('dict1.pkl', 'wb') as f:
    pickle.dump(slownik, f)

with open('dict1.pkl', 'rb') as fh:
    data = pickle.load(fh)

print(type(data))
print(data)
# <class 'dict'>
# {'klucz1': 'wartosc1', 'klucz2': 'wartosc2'}
