import csv

fields = []
rows = []

filename = 'records.csv'
with open(filename, 'r') as f:
    dialect = csv.Sniffer().sniff(f.read(1024))  # wyszukiwanie znaku podziału
    print(f"Dialect delimiter: {dialect.delimiter}")  # Dialect delimiter: ;
    print(f"Dialect qutechar: {dialect.quotechar}")  # Dialect qutechar: "
    # csvreader = csv.reader(f, delimiter=";")
    csvreader = csv.reader(f, delimiter=dialect.delimiter)
    print(csvreader)  # <_csv.reader object at 0x000001C1A78F1180>
    f.seek(0)  # powrót na początek pliku po operacji sniff na 1024 znakch

    # iterator - mozna uzywac go poprzez next() - sekwencyjnie
    fields = next(csvreader)  # next() odczytujemy wiersz i ustawiamy wskażnik na następny

    for row in csvreader:  # odczytujemy od kolejnego wiersza
        rows.append(row)

print(fields)
print(rows)
# ['name;branch;year;cgpa'] błednie ustawiony delimiter
# ['name', 'branch', 'year', 'cgpa']
