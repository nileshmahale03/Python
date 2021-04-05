
#Types
age = 35            #int
name = "Nilesh"     #str
weight = 140.7      #float
is_holiday = False  #bool
is_valid = True     #bool
z = None            #None

print(age)
print(name)
print(weight)
print(is_holiday)
print(is_valid)
print(z)

print(age, name, weight, is_holiday, is_valid, z)

print(type(age), type(name), type(weight), type(is_holiday), type(is_valid), type(z))


#1. Example 1
price = 100
tax = 9.3

total_price = price + tax

print(total_price)

#2. Example 2
# variables are just references to the memory locations
x = 10
y = "IPL"
z = x

print(x)
print(z)

x = 20

print(x)
print(z)

#3. NameError: name 'a' is not defined
#print(a)

#4. using comma to assign multi values to multi variables
x, y, z = 100, "Nilesh", 10.5

print(x, y, z)

x, y = x - 5, y + " Mahale"

print(x, y, z)