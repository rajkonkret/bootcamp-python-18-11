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
        return f"{self.name} (id={self.id})"


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    person_id = Column(ForeignKey('person.id'))
    person = relationship("Person", back_populates='addresses')

    def __str__(self):
        return self.email

    __repr__ = __str__


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

session = Session()

anakin = Person(name='Anakin', age='38')
anakin2 = Person(name='Anakin Akakin', age=38)
anakin2.addresses = [Address(email='anakinkakin@wp.pl')]

session.add(anakin)
session.add(anakin2)
session.commit()
