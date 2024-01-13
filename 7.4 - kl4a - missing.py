# __missing__ - metoda wykonywana gdy nie ma klucza w słowniku

class DefaultDict(dict):
    def __missing__(self, key):
        return "default"





d_python = {}  # pusty słownik
# print(d_python['name'])  # KeyError: 'name'
d_python['name'] = "Radek"
print(d_python['name'])  # Radek

d1 = DefaultDict()
print(d1['name'])  # default - nadpisana metoda __missing__
# zrobic własny słownik, który gdy nie ma klucza w słowniku doda go do słownika z domyslną wartością
