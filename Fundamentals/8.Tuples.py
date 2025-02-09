#Tuples are very similar to lists, but they have one key difference: they are immutable. 
#This means that once a tuple is created, it cannot be changed. 
#We can create a tuple by using parentheses instead of square brackets:

my_tuple = (4, 5, 6)

print(my_tuple)  # Output: (4, 5, 6)

print(my_tuple[0])  # Output: 4
print(my_tuple[1])  # Output: 5
print(my_tuple[2])  # Output: 6

print(my_tuple[1:])  # Output: (5, 6)

#Tuple unpacking
my_tuple = (1, 'hello', 3.14)

# Unpack the tuple into separate variables
a, b, c = my_tuple

# Print the unpacked variables
print("a:", a)  # Output: a: 1
print("b:", b)  # Output: b: hello
print("c:", c)  # Output: c: 3.14

#For tuples, len() returns the number of elements.
#For tuples, count() allows you to count the occurrences of a specified value.
my_tuple = (1, 2, 3, 4, 5)
print("Length of the tuple:", len(my_tuple))  # Output: Length of the tuple: 5

my_tuple = (1, 2, 2, 3, 2, 4, 5, 2)
print("Number of occurrences of 2:", my_tuple.count(2))  # Output: Number of occurrences of 2: 4

