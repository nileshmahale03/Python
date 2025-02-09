#In Python a list is a collection of items that are stored in a specific order.
#Lists are used to store multiple values in a single variable, instead of declaring separate variables for each value.

my_list = [1, 2, 3]

#Lists are mutable
my_list = [1, 2, 3, 4, 5]

my_list[0] = 10
print(my_list)  # Output: [10, 2, 3, 4, 5]

#in/not in operator
my_list = [1, 2, 3]

if 2 in my_list:
    print("2 is in the list")

if 4 not in my_list:
    print("4 is not in the list")

#List Looping
#1. 
my_list = [1, 2, 3, 4, 5]

length = len(my_list)
for i in range(length):
    print(i, my_list[i])

#2. 
my_list = [1, 2, 3, 4, 5]

for element in my_list:
    print(element)

#3. 
my_list = [1, 2, 3, 4, 5]

for i, n in enumerate(my_list):
    print(i, n)

#List Functions 1
my_list = [1, 2, 3, 4, 5]

print(len(my_list))  # Output: 5
print(sum(my_list))  # Output: 15
print(min(my_list))  # Output: 1
print(max(my_list))  # Output: 5

#List Functions 2
#The append() function allows us to to add an item to the end of a list.
#The insert() function allows us to specify the index where we want to insert the new element.
#The remove() function removes the first occurrence of the specified item from the list.
#If you don't tell pop() which item to remove, it will take out the last item in the list.
# You can also tell POP() which item to remove by giving it the position (index) of the item.

my_list = [1, 2, 3, 4, 5]

my_list.append(6)   ; print(my_list)      # Output: [1, 2, 3, 4, 5, 6]
my_list.insert(5, 5); print(my_list)      # Output: [1, 2, 3, 4, 5, 5, 6]
my_list.remove(5)   ; print(my_list)      # Output: [1, 2, 3, 4, 5, 6]
my_list.pop()       ; print(my_list)      # Output: [1, 2, 3, 4, 5]
my_list.pop(1)      ; print(my_list)      # Output: [1, 3, 4, 5]

#List Index
my_list = [1, 2, 3, 4, 5, 3]

print(my_list.index(3))  # Output: 2

#List Slicing
my_list = [1, 2, 3, 4, 5]

print(my_list[1:3])  # Output: [2, 3]
print(my_list[:3])   # Output: [1, 2, 3]
print(my_list[2:])   # Output: [3, 4, 5]
print(my_list[::-1]) # Output: [5, 4, 3, 2, 1]

#List Copy
original_list = [1, 2, 3]
copied_list = original_list.copy()

print(original_list)  # Output: [1, 2, 3]
print(copied_list)  # Output: [1, 2, 3]

# Modifying the copied list doesn't affect the original
copied_list.append(4)

print(original_list)  # Output: [1, 2, 3]
print(copied_list)  # Output: [1, 2, 3, 4]
