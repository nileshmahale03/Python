#1. Example 1
age = 34
name = "Nilesh"
weight = 140.7

print(age)
print(name)
print(weight)

print(age, name, weight)

#1. Example 2
price = 100
tax = 9.3

total_price = price + tax

print(total_price)

#3. Example 3
# variables are just references to the memory locations
x = 10
y = "IPL"
z = x

print(x)
print(z)

x = 20

print(x)
print(z)

#4. Boolean values
is_valid = True

print(is_valid)

#NameError: name 'a' is not defined
#print(a)

# using comma to assign multi values to multi variables
x, y, z = 100, "Nilesh", 10.5

print(x, y, z)

x, y = x - 5, y + " Mahale"

print(x, y, z)