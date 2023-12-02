# słownik
# Typ danych - para klucz wartość, dane oddzielone dwukropkiem (:)
# całośc zamknięta w nawiasy klamrowe  {}
# klucze nie moga się powtarzac

my_dict = {'A': 'one', 'B': 'two', 'C': 'three', 'D': 'four'}
print(my_dict)  # {'A': 'one', 'B': 'two', 'C': 'three', 'D': 'four'}
print(type(my_dict))  # <class 'dict'>

empty_dict = dict()  # pusty słownik
print(empty_dict)  # {}

empty_dict2 = {}  # druga opcja tworzenai pustego słownika
print(empty_dict2)  # {}

dict_with_integer = {1: 'one', 2: "two", 3: 'three'}
print(dict_with_integer)  # {1: 'one', 2: 'two', 3: 'three'}

dict_with_integer2 = dict({1: 'one', 2: "two", 3: 'three'})
print(dict_with_integer2)  # {1: 'one', 2: 'two', 3: 'three'}

dict_mixed = {1: 'one', 'A': 'two', 3: 'three'}
# ctrl alt l
print(dict_mixed)  # {1: 'one', 'A': 'two', 3: 'three'}
print(dict_mixed.keys())  # wypisanie kluczy  dict_keys([1, 'A', 3])
print(dict_with_integer.keys())  # dict_keys([1, 2, 3])
print(dict_mixed.items())
# dict_items([(1, 'one'), ('A', 'two'), (3, 'three')])
print(dict_mixed.values())  # dict_values(['one', 'two', 'three'])
dict_with_list = {1: 'one', 2: 'two', 'A': ['asif', 'jhon', 'maria']}
print(dict_with_list)  # {1: 'one', 2: 'two', 'A': ['asif', 'jhon', 'maria']}
dict_with_list2 = {1: 'one', 2: 'two', 'A': ['asif', 'jhon', 'maria'], "B": ('Bat', 'cat', 'hat')}
print(dict_with_list2)
# {1: 'one', 2: 'two', 'A': ['asif', 'jhon', 'maria'], 'B': ('Bat', 'cat', 'hat')}
dict_with_list3 = {1: 'one',
                   2: 'two',
                   'A': ['asif', 'jhon', 'maria'],
                   "B": ('Bat', 'cat', 'hat'),
                   "C": {"Name", "age", 10}}
print(dict_with_list3)
# {1: 'one', 2: 'two', 'A': ['asif', 'jhon', 'maria'],
#  'B': ('Bat', 'cat', 'hat'), 'C': {'age', 10, 'Name'}}
dict_with_list4 = {1: 'one',
                   2: 'two',
                   'A': ['asif', 'jhon', 'maria'],
                   "B": ('Bat', 'cat', 'hat'),
                   "C": {"Name", "age", 10},
                   "D": {"Name": "Radek", "age": 99}}
print(dict_with_list4)

# tworzenie słownika z sekwencji kluczy
keys = {'a', "b", 'c', 'd'}  # uzylismy seta bo klucze nie mogą sie powtarzac
my_dict2 = dict.fromkeys(keys)
print(my_dict2)  # {'b': None, 'a': None, 'c': None, 'd': None}
# None - nic, nie wiem, to zależy
print({"czy_pali": None})
value = 10
my_dict3 = dict.fromkeys(keys, value)
print(my_dict3)  # {'a': 10, 'c': 10, 'd': 10, 'b': 10}
value2 = [10, 20, 30]
my_dict4 = dict.fromkeys(keys, value2)
print(my_dict4)  # {'d': [10, 20, 30], 'b': [10, 20, 30], 'a': [10, 20, 30], 'c': [10, 20, 30]}

# wypisywanie danych ze słownika
print(my_dict["A"])  # one
# powypisywac z tych słowników wybrane klucze
print(my_dict4['a'])  # [10, 20, 30]

print(my_dict4.get("a"))  # [10, 20, 30]
print(my_dict4.get("e"))  # None
# print(my_dict4['e'])  # KeyError: 'e'
# mozemy ustawić domyślną wartość jaka będzie zwracana gdy klucza nie ma w słowniku
print(my_dict4.get("e", "Nie ma"))  # Nie ma

my_dict5 = {'Name': "Radek", "ID": 12345, 'DOB': 1991, 'Address': "Warsaw"}
print(my_dict5)  # {'Name': 'Radek', 'ID': 12345, 'DOB': 1991, 'Address': 'Warsaw'}

my_dict5['DOB'] = '1980'
print(my_dict5)  # {'Name': 'Radek', 'ID': 12345, 'DOB': '1980', 'Address': 'Warsaw'}
my_dict5['Address'] = 'Warsaw Bemowo'
print(my_dict5)  # {'Name': 'Radek', 'ID': 12345, 'DOB': '1980', 'Address': 'Warsaw Bemowo'}

dict1 = {'DOB': 1995}
print(type(dict1))  # <class 'dict'>  ctrl alt l
print(dict1)  # {'DOB': 1995}

my_dict5.update(dict1)
print(my_dict5)  # {'Name': 'Radek', 'ID': 12345, 'DOB': 1995, 'Address': 'Warsaw Bemowo'}

my_dict5['Job'] = 'Developer'
print(my_dict5)  # {'Name': 'Radek', 'ID': 12345, 'DOB': 1995, 'Address': 'Warsaw Bemowo', 'Job': 'Developer'}

dict2 = {"cpi": 3.4}  # float, zmiennoprzecinkowe
my_dict5.update(dict2)
print(
    my_dict5)  # {'Name': 'Radek', 'ID': 12345, 'DOB': 1995, 'Address': 'Warsaw Bemowo', 'Job': 'Developer', 'cpi': 3.4}

print(my_dict5.pop("cpi"))  # 3.4

print(my_dict5)
# {'Name': 'Radek', 'ID': 12345, 'DOB': 1995, 'Address': 'Warsaw Bemowo', 'Job': 'Developer'}

print(my_dict5.popitem())  # ('Job', 'Developer')
print(my_dict5)
# {'Name': 'Radek', 'ID': 12345, 'DOB': 1995, 'Address': 'Warsaw Bemowo'}

del [my_dict5['ID']]
print(my_dict5)  # {'Name': 'Radek', 'DOB': 1995, 'Address': 'Warsaw Bemowo'}

my_dict5.clear()  # usunięcie wszystkich elemntów ze słownika
print(my_dict5)  # {} - pusty słownik
del my_dict5  # usunięcie słownika  zpamięci
# print(my_dict5)  # NameError: name 'my_dict5' is not defined. Did you mean: 'my_dict'?

# zmiana nazwy klucza w słowniku
slownik = {'stary_klucz': 'wartosc'}
slownik["nowy_klucz"] = slownik.pop('stary_klucz')
print(slownik)
# {'nowy_klucz': 'wartosc'}

# kopiowanie słownika
my_dict5 = {'Name': "Radek", "ID": 12345, 'DOB': 1991, 'Address': "Warsaw"}
my_dict_copy_ref = my_dict5  # kopia referencji, adresu w pamięci
my_dict_copy = my_dict5.copy()  # kopia elementów słownika do nowego słownika
print(my_dict_copy_ref)  # {'Name': 'Radek', 'ID': 12345, 'DOB': 1991, 'Address': 'Warsaw'}
my_dict5.clear()
print(my_dict_copy_ref)  # {}
print(id(my_dict5), id(my_dict_copy_ref))  # 2179643317760 2179643317760
print(my_dict_copy)  # {'Name': 'Radek', 'ID': 12345, 'DOB': 1991, 'Address': 'Warsaw'}

dict3 = {"x": 2}
print(dict3)
dict3.update([('y', 3), ('z', 0)])
print(dict3)  # {'x': 2, 'y': 3, 'z': 0}

# napisac programm, który bedzie działął jak słownik polsko-angielski
# podajemy wyraz -> tłumaczenie
# stworzyc słownik
# wyswietlic uzytkownikowi klucze
# pobrac od uzytkownika słowo, które chce przetłumaczyc input()
# wyswietlic tłumaczenie

word_to_translate = {'name': 'imie', 'cat': 'kot', 'water': 'woda'}
print(word_to_translate.keys())
odp = input("Podaj słówko do przetłumaczenia")
print(word_to_translate.get(odp.lower().replace(" ", "")))

# kalkulator
# pobrać dwie liczby
# wypisac wynik działania (dodawania)
