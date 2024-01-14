# __lt__ , __le__, __gt__, __ge__, __eq__
# __ne__
from functools import total_ordering


# @total_ordering pozwala na zdefiniowanie tylko dwóch z tych metod
# (jednej z pierwszej grupy: __lt__, __le__, __gt__, __ge__ i __eq__),
# a reszta jest automatycznie wnioskowana.

@total_ordering
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        return self.grade == other.grade

    def __lt__(self, other):
        return self.grade < other.grade


alice = Student("Alice", 90)
bob = Student("Bob", 85)

print(alice < bob)  # False
print(alice >= bob)  # True
