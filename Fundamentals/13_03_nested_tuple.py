#nested tuple

nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(nested_tuple)
# Outputs: ((1, 2, 3), (4, 5, 6), (7, 8, 9))

nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(nested_tuple[1])  # Outputs: (4, 5, 6)

nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(nested_tuple[1][2])  # Outputs: 6

nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
for inner_tuple in nested_tuple:
    for element in inner_tuple:
        print(element, end=" ")
# Outputs: 1 2 3 4 5 6 7 8 9

matrix = ((1, 0), (0, 1))
print(matrix[0][1])  # Outputs: 0

#Tuple Unpacking

person = ("Alice", 25, "Engineer")
name, age, profession = person
print(name)       # Outputs: Alice
print(age)        # Outputs: 25
print(profession) # Outputs: Engineer

numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(first)  # Outputs: 1
print(middle) # Outputs: [2, 3, 4]
print(last)   # Outputs: 5

x, y = 10, 20
x, y = y, x
print(x)  # Outputs: 20
print(y)  # Outputs: 10
