# relacje w bazach danych
# Typ relacji
# Opis
# Jeden do jednego	Obydwie tabele mogą zawierać tylko jeden rekord po każdej stronie relacji.
# Każda wartość klucza podstawowego dotyczy tylko jednego lub nie dotyczy żadnego rekordu w tabeli powiązanej.
# Relacje "jeden do jednego" są w większości wymuszane przez reguły biznesowe i nie wynikają w sposób naturalny z danych.
# Jeśli taka reguła nie obowiązuje, możliwe jest łączenie obydwu tabel bez naruszania reguł normalizacji.
#
# Jeden do wielu	Tabela klucza podstawowego zawiera tylko jeden rekord, który dotyczy żadnego,
# jednego lub wielu rekordów w powiązanej tabeli.

# Wiele do wielu	Każdy rekord w obydwu tabelach może się odnosić do dowolnej liczby rekordów
# lub nie odnosić się do żadnego z rekordów w drugiej tabeli.
# W przypadku takich relacji wymagana jest trzecia tabela nazywana tabelą powiązań,
# ponieważ systemy relacyjne nie mogą bezpośrednio obsługiwać takiej relacji.
from sqlalchemy import (
    Column, Integer, String, ForeignKey, create_engine
)

from sqlalchemy.orm import relationship, sessionmaker, declarative_base

# engine = create_engine('sqlite:///:memory:')
engine = create_engine('sqlite:///adress_book.db', echo=True)
Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(String)
    addresses = relationship(
        'Address',
        back_populates='person',
        order_by='Address.email',
        cascade='all, delete-orphan'
    )

    def __repr__(self):
        return f"{self.name} (id={self.id})"  # Anakin(id=2)


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    person_id = Column(ForeignKey('person.id'))
    person = relationship("Person", back_populates='addresses')

    def __str__(self):
        return self.email

    __repr__ = __str__  # a = 7


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

session = Session()

anakin = Person(name='Anakin', age='38')
anakin2 = Person(name='Anakin Akakin', age=38)
anakin2.addresses = [Address(email='anakinkakin@wp.pl')]
obi = Person(name="Obi Wan Kenobi", age=45)
obi.addresses = [
    Address(email='obi@example.com'),
    Address(email='waaka@example.com')
]

session.add(anakin)
session.add(anakin2)
session.add(obi)

session.commit()

all_ = session.query(Person).all()
print(all_)
# [Anakin(id=1), Anakin(id=2), Anakin Akakin(id=3), Anakin(id=4), Anakin Akakin(id=5), Obi Wan Kenobi(id=6), Anakin(id=7),
#  Anakin Akakin(id=8), Obi Wan Kenobi(id=9)]

an1 = session.query(Person).first()
print(an1)  # Anakin (id=1)
print(type(an1))  # <class '__main__.Person'>
print(an1.name, an1.age)  # Anakin 38

obi_list = session.query(Person).filter(
    Person.name.like('Obi%')
).all()

print(obi_list)
# [Obi Wan Kenobi (id=6),
#  Obi Wan Kenobi (id=9),
#  Obi Wan Kenobi (id=12),
#  Obi Wan Kenobi (id=15),
#  Obi Wan Kenobi (id=18),
#  Obi Wan Kenobi (id=21)]

# wyswietlic name, age, address
for o in obi_list:
    print("id=", o.id, 'name:', o.name, "wiek:", o.age, "email:", o.addresses)
# id= 24 name: Obi Wan Kenobi wiek: 45 email: [obi@example.com, waaka@example.com]
# id= 6 name: Obi Wan Kenobi wiek: 45 email: [obi@example.com, waaka@example.com]
# id= 9 name: Obi Wan Kenobi wiek: 45 email: [obi@example.com, waaka@example.com]
# id= 12 name: Obi Wan Kenobi wiek: 45 email: [obi@example.com, waaka@example.com]
# id= 15 name: Obi Wan Kenobi wiek: 45 email: [obi@example.com, waaka@example.com]
# id= 18 name: Obi Wan Kenobi wiek: 45 email: [obi@example.com, waaka@example.com]
# id= 21 name: Obi Wan Kenobi wiek: 45 email: [obi@example.com, waaka@example.com]
# id= 24 name: Obi Wan Kenobi wiek: 45 email: [obi@example.com, waaka@example.com]
# id= 27 name: Obi Wan Kenobi wiek: 45 email: [obi@example.com, waaka@example.com]
# id= 30 name: Obi Wan Kenobi wiek: 45 email: [obi@example.com, waaka@example.com]
