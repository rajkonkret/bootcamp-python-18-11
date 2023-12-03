# pliki csv - pliki, gdzie dane oddzielone są znakiem podziału
# Marcin, Radek, Karolina
import csv  # moduł do działąń z plikami csv

fields = ['name', 'branch', 'year', 'cgpa']
row = ['radek', 'coe', '3', '0']

zipped_dict = dict(zip(fields, row))
print(zipped_dict)  # {'name': 'radek', 'branch': 'coe', 'year': '3', 'cgpa': '0'}

dict_list = [
    {'name': 'radek', 'branch': 'coe', 'year': '3', 'cgpa': '0'},
    {'name': 'tomek', 'branch': 'cos', 'year': '3', 'cgpa': '8'},
    {'name': 'zenek', 'branch': 'cot', 'year': '3.9', 'cgpa': '9'},
    {'name': 'marek', 'branch': 'coe', 'year': '11', 'cgpa': '1.5'},
    {'name': 'arek', 'branch': 'cow', 'year': '8', 'cgpa': '0.2'},
]
with open("records.csv", 'w', newline="") as csv_f:
    # newline="" oznaczenie, ze nie chcemy pustych lini pomiędzy wierszami

    # csvwriter = csv.writer(csv_f)
    # csvwriter.writerow(fields)
    # csvwriter.writerow(row)
    # csv pozwala nam pracować z danymi umieszczonymi w słowniku
    cswriter = csv.DictWriter(csv_f, fieldnames=fields, delimiter=";")
    cswriter.writeheader()
    cswriter.writerow(zipped_dict)  # zapis z pojedynczego słownika
    cswriter.writerows(dict_list)  # zapis z listy słowników
