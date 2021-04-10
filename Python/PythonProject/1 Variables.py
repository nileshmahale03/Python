
"""
1. Variables are just references to the memory locations
2. Variables Types:
    1. int
    2. str
    3. float
    4. bool
    5. NoneType
3. Use commas to assign multi-values to multi variables
4. type() : get type of variable
5. id()   : get memory location
6. is     : operator returns boolean value
"""

age = 35
name = "Nilesh"
weight = 140.7
isMarried, isHomeOwner = True, False
numberOfKids = None

print(age, name, weight, isMarried, isHomeOwner, numberOfKids)

print(type(age), type(name), type(isMarried), type(isHomeOwner), type(numberOfKids))

#1. Variables are just references to the memory locations
x = 10
z = x

print(x, z)
print(id(x), id(z))
print(x is z)

x = 20

print(x, z)
print(id(x), id(z))
print(x is z)

"""
Problem: Swap 2 variables:
I/P: a = 100, b = 20
O/p: a = 20,  b = 100
"""

a, b = 100, 20
print(a, b)

#using extra variable
temp = a
a = b
b = temp

print(a, b)

#using comma assignment
a, b = b, a

print(a, b)