# __missing__ - metoda wykonywana gdy nie ma klucza w słowniku

class DefaultDict(dict):
    def __missing__(self, key):
        return "default"


class AutoKeyDict(dict):
    def __missing__(self, key):
        self[key] = 0
        return key


class CaseInsesitiveDict(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            return self.get(key.lower())


d_python = {}  # pusty słownik
# print(d_python['name'])  # KeyError: 'name'
d_python['name'] = "Radek"
print(d_python['name'])  # Radek

d1 = DefaultDict()
print(d1['name'])  # default - nadpisana metoda __missing__
# zrobic własny słownik, który gdy nie ma klucza w słowniku doda go do słownika z domyslną wartością

d2 = AutoKeyDict()
print(d2)
print(d2['name'])  # name
print(d2)  # {'name': 0}
d2['name'] = "Radek"
print(d2['name'])  # Radek

# słownik, który potrafi korzystac z klucza niezależnie czy zostanie podany jako małe czy duże litery
# print(1.lower())  # SyntaxError: invalid decimal literal
d3 = CaseInsesitiveDict()
d3['name'] = 'Radek'
print(d3['Name'])  # Radek
