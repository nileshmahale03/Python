#Syntax
#{key_expression: value_expression for item in iterable if condition}

squares = {x: x**2 for x in range(1, 6)}
print(squares)
# Outputs: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

numbers = range(1, 10)
even_numbers = {x: x**2 for x in numbers if x % 2 == 0}
print(even_numbers)
# Outputs: {2: 4, 4: 16, 6: 36, 8: 64}

original = {"Alice": 85, "Bob": 90, "Charlie": 78}
reversed_dict = {value: key for key, value in original.items()}
print(reversed_dict)
# Outputs: {85: 'Alice', 90: 'Bob', 78: 'Charlie'}

marks = {"Alice": 85, "Bob": 90, "Charlie": 78}
status = {key: ("Pass" if value >= 80 else "Fail") for key, value in marks.items()}
print(status)
# Outputs: {'Alice': 'Pass', 'Bob': 'Pass', 'Charlie': 'Fail'}

table = {x: {y: x * y for y in range(1, 6)} for x in range(1, 6)}
print(table)
# Outputs: {1: {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}, 2: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}, ...}


