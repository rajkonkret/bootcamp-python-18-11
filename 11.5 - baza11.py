from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()


# jeden do wielu 1:N
class Parent(Base):
    __tablename__ = 'parents'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))  # maksymalna długość tekstu
    children = relationship("Child", backref='parent')  # backref - doda pole parent w kalsie Child automatycznie
    # przy back_populate musieliśmy w klasie Child samo zdefiniowac to pole z odpowiednią realcją


class Child(Base):
    __tablename__ = 'children'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    parent_id = Column(Integer, ForeignKey('parents.id'))


engine = create_engine('sqlite:///:memory:', echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

parent = Parent(name="Rodzic")
child1 = Child(name="Dziecko 1", parent=parent)
child2 = Child(name="Dziecko 2", parent=parent)

# session.add(parent)
# session.add(child1)
# session.add(child2)
session.add_all(
    [parent, child1, child2]
)
session.commit()

our_parent = session.query(Parent).all()
print(our_parent)
# filter_by - filtrowanie po wskazanym polu i wartosci
our_parent_filtered = session.query(Parent).filter_by(name="Rodzic").first()
print(f"Rodzic: {our_parent_filtered.name}")
for child in our_parent_filtered.children:
    print(f"Dziecko: {child.name}")
    print(f"Rodzic: {child.parent.name}")
# Rodzic: Rodzic
# 2024-02-10 14:24:53,316 INFO sqlalchemy.engine.Engine SELECT children.id AS children_id, children.name AS children_name,
# children.parent_id AS children_parent_id
# FROM children
# WHERE ? = children.parent_id
# 2024-02-10 14:24:53,316 INFO sqlalchemy.engine.Engine [generated in 0.00005s] (1,)
# Dziecko: Dziecko 1
# Dziecko: Dziecko 2
