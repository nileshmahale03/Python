#Sets

'''
1. A set is unordered
2. A set can only contain unique elements
3. A set can be created using curly braces {}
'''

my_set = set()

my_set.add(1)
my_set.add(2)
my_set.add(1)

print(my_set)  # Output: {1, 2}

#Set Operations
my_set = {1, 2, 3}

my_set.remove(2)
print(my_set)  # Output: {1, 3}

my_set.remove(4)  # Raises KeyError

#Sets Looping
my_set = {1, 2, 3}

for element in my_set:
    print(element)

#Convert List to Sets
my_list = [1, 2, 3, 4, 5, 1, 2, 5]

my_set = set(my_list)
print(my_set)  # Output: {1, 2, 3, 4, 5}
my_list_no_duplicates = list(my_set)
print(my_list_no_duplicates)

#in Keyword
my_set = {"Cat", "Dog", "Mouse"}

contains_cat = "Cat" in my_set   # True
contains_lion = "Lion" in my_set # False
print(contains_cat, contains_lion)

