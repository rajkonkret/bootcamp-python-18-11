import chardet

# pip install chardet

with open('test.log', 'rt') as file:
    lines = file.read()

print(lines)  # DoĹ›dane

with open('test.log', 'rt', encoding='utf-8') as file:
    lines = file.read()

print(lines)  # Dośdane

file_path = 'test.log'
with open(file_path, 'rb') as file:  # rb - odczyt bajtowy(binarny)
    raw_data = file.read()

result = chardet.detect(raw_data)
print(result)
# {'encoding': 'Windows-1254', 'confidence': 0.6847895417292195, 'language': 'Turkish'}
# pozwiększeniu próbki (dodaniu wiecej polskich znaków w tekście w pliku)
# mamy poprawny wynik
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
encoding = result['encoding']
print(encoding)  # utf-8
print(raw_data.decode(encoding=encoding))
# utf-8
# Radek
# Dodane
# Dodane
# Dośdane
# Dośąćńdane
