import shutil
from pathlib import Path

base_path = Path('ops_example')
base_path2 = Path('ops_example/D')

if base_path.exists() and base_path.is_dir():
    """Recursively delete a directory tree."""
    shutil.rmtree(base_path)  # usuniecie drzewa katalogów

# utworzenie katalogu
base_path.mkdir()

path_b = base_path / 'A' / 'B'  # ops_example/A/B
path_c = base_path / 'A' / 'C'
path_d = base_path / 'A' / 'D'

path_b.mkdir(parents=True)  # parents=True bo musi jeszcze utworzyc katalog A zanim utworzy C
path_c.mkdir()  # tu katalog A juz był wiec umie utworzyc C

for filename in ('ex1.txt', 'ex2.txt', 'ex3.txt'):
    with open(path_b / filename, 'w', encoding='utf-8') as stream:
        stream.write(f"Jakaś treść w pliku {filename}")
        # ops_example/A/B/ex1.txt

# przenosi do katalogu D pliki, usuneło katalog B
shutil.move(path_b, path_d)
ex1 = path_d / 'ex1.txt'
# zmian nazwy pliku
ex1.rename(ex1.parent / 'ex1renamed.log')

print(base_path.absolute())
# /Users/radoslawjaniak/PycharmProjects/bootcamp-python-18-11/ops_example

print(base_path.name)  # ops_example
print(base_path.parent.absolute())
# /Users/radoslawjaniak/PycharmProjects/bootcamp-python-18-11

print(base_path.suffix)
print(ex1.suffix)  # .txt
print(base_path.parts)  # ('ops_example',)
print(base_path2.parts)  # ('ops_example', 'D')
