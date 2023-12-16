# listy składane - lista w jedej linijce
# list comprehensions
# [expression for item in iterable]

numbers = [1, 2, 3, 4, 5]

# tworzenie nowej listy
squared = [num ** 2 for num in numbers]
print(f"Squared: {squared}")  # Squared: [1, 4, 9, 16, 25]

even_numbers = [num for num in numbers if num % 2 == 0]
print(f"Even: {even_numbers}")  # Even: [2, 4]

modifed_numbers = [num * 2 if num % 2 == 0 else num for num in numbers]
print(f"Zmodyfikowane: {modifed_numbers}")  # Zmodyfikowane: [1, 4, 3, 8, 5]

modifed_numbers2 = []
for num in numbers:
    modifed_numbers2.append(num * 2 if num % 2 == 0 else num)
print(f"Zmodyfikowane2: {modifed_numbers2}")  # Zmodyfikowane: [1, 4, 3, 8, 5]

even_odd = ['parzysta' if x % 2 == 0 else 'nieparzysta' for x in numbers]
print(f"Parzyste - Nieparzyste: {even_odd}")
# Parzyste - Nieparzyste: ['nieparzysta', 'parzysta', 'nieparzysta', 'parzysta', 'nieparzysta']

numbers2 = [-2, -3, 3, 4, -7]
absolute = [abs(x) for x in numbers2]
print(f"Wartości absolutne: {absolute}")  # Wartości absolutne: [2, 3, 3, 4, 7]

word = "Python"
print(list(word))  # ['P', 'y', 't', 'h', 'o', 'n']

letters = [letter for letter in word]
print(letters)  # ['P', 'y', 't', 'h', 'o', 'n']
