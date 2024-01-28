# ORM - Mapowanie obiektowo-relacyjne, w skrócie ORM, to nowoczesne podejście do zagadnienia współpracy z bazą danych.
# Jego cechą charakterystyczną jest wykorzystanie filozofii programowania obiektowego.
# zamiana obiektów na tabele w bazie danych
# korzystamy z bazy danych poprzez bibliotekę a nie za pomocą komend sql

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# pip install sqlalchemy
# https://mindboxgroup.com/pl/co-to-jest-orm-oraz-czym-sie-rozni-od-sql-object-relational-mapping/

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(name={self.name}, age={self.age})>"


# Tworzymy połączenie do bazy (zwraca nam silnik)
# echo=True - logowanie zdarzeń z bazy
engine = create_engine('sqlite:///mydatabase.db', echo=True)
Base.metadata.create_all(engine)  # Tworzy tabele w bazie

# utworzenie obiektu sesji za pomocą bedziemy łaczyć sie z bazą danych
Session = sessionmaker(bind=engine)
session = Session()  # obiekt sesji, zbliżony do cursor w bibliotece sqlite3

new_user = User(name='Jan kowalski', age=30)
session.add(new_user)  # INSERT INTO users (name, age) VALUES (?, ?)
session.commit()
session.close()

users = session.query(User).all()  # select na bazie, odczyt danych
# SELECT users.id AS users_id, users.name AS users_name, users.age AS users_age
# FROM users
for user in users:
    print(user)
# <User(name=Jan kowalski, age=30)>
# <User(name=Jan kowalski, age=30)>
# <User(name=Jan kowalski, age=30)>
# <User(name=Jan kowalski, age=30)>
# <User(name=Jan kowalski, age=30)>
