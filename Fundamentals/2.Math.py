#Max /Min Int
float("inf")
float("-inf")

#Arithmetic Operators
x, y = 3, 6

print(x + y)  # Output: 9
print(x - y)  # Output: -3
print(x * y)  # Output: 18
print(y / x)  # Output: 2.0 - Division is float, Integer Division is integer

x, y = 7, 2

print(x // y) # Output: 3  (7 divided by 2 is 3.5, after rounding down we get 3)
print(x % y)  # Output: 1  (7 divided by 2 is 3, with a remainder of 1)
print(x ** y) # Output: 49 (7 raised to the power of 2 is 49, 7*7 = 49)

#Comparison Operators
x, y = 3, 5
print(x == y)  # Output: False

'''
The comparison operators are:

==  Equal to
!=  Not equal to
<   Less than
>   Greater than
<=  Less than or equal to
>=  Greater than or equal to
'''

#Shorthand Operators
count = 0
count += 1
count += 2
print(count)  # Output: 3

#Boolean or/and
a = True
b = False
print(a or b)   # Output: True
print(a and b)  # Output: False
print(not a)    # Output: False
print(not b)    # Output: True

'''
truth table for the OR/AND operation is as follows

A	B	A or B   A and B
False	False	False    False
True	False	True     False
False	True	True     False
True	True	True     True

To summarize, the OR operation returns True if at least one of the operands is True.
To summarize, the AND operation returns True if both of the operands is True. 
'''


