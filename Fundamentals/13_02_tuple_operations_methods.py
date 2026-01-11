# +
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2
print(result)  # Outputs: (1, 2, 3, 4, 5, 6)

# *
tuple1 = (1, 2)
result = tuple1 * 3
print(result)  # Outputs: (1, 2, 1, 2, 1, 2)

# in/not in
tuple1 = (1, 2, 3)
print(2 in tuple1)    # Outputs: True
print(4 not in tuple1)  # Outputs: True

# slicing
tuple1 = (1, 2, 3, 4, 5)
print(tuple1[1:4])  # Outputs: (2, 3, 4)
print(tuple1[::2])  # Outputs: (1, 3, 5)

# len()
tuple1 = (1, 2, 3)
print(len(tuple1))  # Outputs: 3

# max(), min()
numbers = (5, 1, 8, 3)
print(max(numbers))  # Outputs: 8
print(min(numbers))  # Outputs: 1

# sum()
numbers = (1, 2, 3, 4)
print(sum(numbers))  # Outputs: 10

# sorted()
numbers = (3, 1, 4, 2)
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Outputs: [1, 2, 3, 4]

# .count()
tuple1 = (1, 2, 2, 3, 2)
print(tuple1.count(2))  # Outputs: 3

# .index()
tuple1 = (1, 2, 3, 4)
print(tuple1.index(3))  # Outputs: 2

#Immutability of Tuples
tuple1 = (1, 2, 3)
# tuple1[0] = 4  # This will raise a TypeError
tuple2 = (4,) + tuple1[1:]
print(tuple2)  # Outputs: (4, 2, 3)
