# json - obiekt typu para klucz wartość
# {
#   "menu": {
#     "id": "file",
#     "value": "File",
#     "popup": {
#       "menuitem": [
#         {"value": "New", "onclick": "CreateNewDoc()"},
#         {"value": "Open", "onclick": "OpenDoc()"},
#         {"value": "Close", "onclick": "CloseDoc()"}
#       ]
#     }
#   }
# }
# w pythonie łatwo zamienic json na słownik - typy podobne do siebie
# None -> null
import json

person_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(person_dict))  # <class 'dict'>

with open('nasze_dane.json', 'w') as f:
    json.dump(person_dict, f)
# {"name": "Radek", "age": 40, "czy_pali": null}

with open('nasze_dane.json', 'w') as f:
    json.dump(person_dict, f, indent=4)
# {
#     "name": "Radek",
#     "age": 40,
#     "czy_pali": null
# }

with open('nasze_dane.json', 'w') as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)
# {
#     "age": 40,
#     "czy_pali": null,
#     "name": "Radek"
# }

# odczyt jsona z pliku i parsowanie na słownik
with open('nasze_dane.json', 'r') as file:
    data = json.load(file)

print(data)  # {'age': 40, 'czy_pali': None, 'name': 'Radek'}
print(type(data))  # <class 'dict'>
print(data['name'])  # Radek

# zamiana słownika na jsona - zmiana na str wygladający jak json
json_text = json.dumps(data)
print(json_text)  # {"age": 40, "czy_pali": null, "name": "Radek"}

# zamiana jsona (str) na słownik pythonowy
string_json = json.loads(json_text)
print(string_json)
print(type(string_json))
# {"age": 40, "czy_pali": null, "name": "Radek"} - json czyli str odpowiednio sformatowany
# {'age': 40, 'czy_pali': None, 'name': 'Radek'} - to jest słownik
# <class 'dict'>
