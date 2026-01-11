#list comprehension
#[expression for item in iterable if condition]

numbers = [x for x in range(10)]
print(numbers)

squared = [x**2 for x in range(10)]
print(squared)

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

pairs = [(x, y) for x in range(3) for y in range(3)]
print(pairs)

names = ["alice", "bob", "charlie"]
uppercase_names = [name.upper() for name in names]
print(uppercase_names)

categories = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(categories)

nested_list = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested_list for item in sublist]
print(flattened)