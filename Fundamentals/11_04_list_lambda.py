#lambda

#lambda arguments: expression
square = lambda x: x ** 2
print(square(5))

add = lambda a, b: a + b
print(add(3, 5))

#map(function, iterable)
numbers = [1, 2, 3, 4]
doubled = map(lambda x: x ** 2, numbers)
print(list(doubled))

#filter(function, iterable)
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))

'''
from functools import reduce
reduce(function, iterable)
'''
from functools import reduce
numbers = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, numbers)
print(total)

words = ["apple", "banana", "cherry", "date"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)
