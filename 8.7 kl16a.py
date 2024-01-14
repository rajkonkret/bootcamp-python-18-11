import pickle
from kl10 import Person

with open('dane.pickle', 'rb') as file:
    p = pickle.load(file)

print(p)
print(type(p))  # <class 'list'>
# [Person(first_name='Jan', last_name='Kowalski', id=1), Person(first_name='Maciej', last_name='Nowak', id=2)]
# <class 'list'>

# wypisac z listy obiekty
for person in p:
    print(person)
    # Person(first_name='Jan', last_name='Kowalski', id=1)
    # Person(first_name='Maciej', last_name='Nowak', id=2)

for person in p:
    person.greets()
# Witam, jestem Jan Kowalski, Td to 1
# Witam, jestem Maciej Nowak, Td to 2
