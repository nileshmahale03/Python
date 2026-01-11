#tuples
#similar to list but immutable
#ordered, immutable, allow duplicates, heterogenous data, hashable

#common use cases
#1
point = (4, 5)
print(point, type(point))

#2
def cal_stats(numbers):
    return (min(numbers), max(numbers), sum(numbers)/len(numbers))

stats = cal_stats([10, 20, 30])
print(stats)

#3
days_of_week = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
print(days_of_week)

#Creating Tuples
#1. using ()
fruits = ("apple", "banana", "cherry")
print(fruits)

#2. empty tuple
empty_tuple = ()
print(empty_tuple)

#3. single-element tuple
sin_ele_tup = (42,)
print(sin_ele_tup)

#4. tuple() constructor
list = [1, 2, 3]
from_list = tuple(list)
print(from_list)

string = "hello"
from_string = tuple(string)
print(from_string)

#5. taking user input
int_tuple = tuple(map(int, input().split()))

#Accessing tuple elements

#1. +ve indices
fruits = ("apple", "banana", "cherry")
print(fruits[0])  # Outputs: apple
print(fruits[1])  # Outputs: banana

#2. -ve indices
fruits = ("apple", "banana", "cherry")
print(fruits[-1])  # Outputs: cherry
print(fruits[-2])  # Outputs: banana

#3. slicing
fruits = ("apple", "banana", "cherry", "date")
print(fruits[1:3])  # Outputs: ('banana', 'cherry')
print(fruits[:2])   # Outputs: ('apple', 'banana')
print(fruits[::2])  # Outputs: ('apple', 'cherry')  # Every second element

#Immutability of Tuples
fruits = ("apple", "banana", "cherry")
# fruits[0] = "orange"  # This will raise a TypeError
