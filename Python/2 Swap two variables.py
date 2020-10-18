#Swap two variables
#I/P: x = 100, y = 20
#O/P: x = 20, y = 100

x = 100
y = 20

print(x, y)

"""
# Wrong approach
x = y
y = x

print(x, y)

"""

#using extra variable
z = x

x = y

y = z

print(x, y)

#using comma assignment

x, y = y, x

print(x, y)