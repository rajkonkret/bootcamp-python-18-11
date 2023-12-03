def connect(**opcje):  # ** - argumenty słownikowe
    print(opcje)
    print(type(opcje))  # <class 'dict'>
    param = {
        'host': '127.0.0.1',
        'port': '8080'
    }
    param.update(opcje)  # słownik opcje dodany jako kolejne klucze do słownik param
    print(param)  # {'host': '127.0.0.1', 'port': '8080', 'a': 7, 'b': 9, 'name': 'Radek'}
    param['pwd'] = opcje
    print(param)
    # {'host': '127.0.0.1', 'port': '8080', 'a': 7, 'b': 9, 'name': 'Radek',
    #  'pwd': {'a': 7, 'b': 9, 'name': 'Radek'}}
    # opcje dodoany jako słownik do klucza 'pwd'


connect()  # {}
# nie mozemy podac argumentów pozycyjne
# connect(1)  # TypeError: connect() takes 0 positional arguments but 1 was given
connect(a=7)  # argumenty podane po nazwie  {'a': 7}
connect(name="Radek")  # {'name': 'Radek'}
connect(a=7, b=9, name="Radek")  # {'a': 7, 'b': 9, 'name': 'Radek'}


# * - wszystkie argumenty pozycyjne
# ** - przyjmie wszystkie nazwane
def connect_all(*args, **kwargs):
    print(args, kwargs)


connect_all()  # () {}
connect_all(1, 2, 3, 4)
connect_all(1, 2, 3, 4, "zenek")
connect_all(1, 2, 3, 4, "zenek", a=9, b=8)
# (1, 2, 3, 4) {}
# (1, 2, 3, 4, 'zenek') {}
# (1, 2, 3, 4, 'zenek') {'a': 9, 'b': 8}
