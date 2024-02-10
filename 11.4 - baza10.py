from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

engine = create_engine("sqlite:///moja_baza_danych.db")
Base = declarative_base()


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    books = relationship('Book', back_populates='author')


class Publisher(Base):
    __tablename__ = 'publishers'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    books = relationship("Book", back_populates='publisher')


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))  # dostajemy id autora
    publisher_id = Column(Integer, ForeignKey('publishers.id'))

    author = relationship("Author", back_populates='books')  # zostaja zmapowane(zamienione) na obiekty klasy Author
    publisher = relationship("Publisher", back_populates='books')


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# new_author = Author(name='Adam Mickiewicz')
# new_publisher = Publisher(name='Wydawnictwo XYZ')
# new_book = Book(title="Pan Tadeusz", author=new_author, publisher=new_publisher)
#
# session.add_all(
#     [new_author, new_publisher, new_book]
# )
new_author = Author(name='Jan Kowalski')
new_publisher = Publisher(name='Wydawnictwo ABC')
new_book = Book(title="Nauka Pythona od podstaw", author=new_author, publisher=new_publisher)

session.add_all(
    [new_author, new_publisher, new_book]
)

session.commit()
# odczytac z bazy autorów i z autorów odczytać ich ksiązki
# z ksiązęk odczytać wydawców
# wypisać autor, ksiązka, wydawca

authors = session.query(Author).all()
print(authors)
for author in authors:
    print(f"Author: {author.name}")
    for b in author.books:
        # print(b)
        print(f"Ksiązka: {b.title}, wydawca: {b.publisher.name}")  # Ksiązka: Pan Tadeusz, wydawca: Wydawnictwo XY
        print(f"Ksiązka: {b.title}, wydawca: {b.publisher}")
    # Ksiązka: Pan Tadeusz, wydawca: <__main__.Publisher object at 0x10514a5a0>
# Author: Adam Mickiewicz
# Ksiązka: Pan Tadeusz, wydawca: Wydawnictwo XYZ

# wypisac wydawców i ich ksiazki
publishers = session.query(Publisher).all()
for publisher in publishers:
    print(f"Wydawca: {publisher.name}")
    for book in publisher.books:
        print(f"Ksiązka: {book.title}")
