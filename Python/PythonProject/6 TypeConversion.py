
"""
Type conversion is Python:

Implicit
    boolean automatically upgrades to integer
    integer automatically upgrades to float
Explicit
"""

#1.
a = True
b = 1
c = a + b
print(c)

#2.
a = 135
b = 10.5
c = a + b
print(c)
print(type(c))

#3.
a = "123"
b = 5
c = int(a) + b
print(c)

#4.
str = "NILESH MAHALE"
l = list(str)
t = tuple(str)
s = set(str)

print(str)
print(l)
print(t)
print(s)

#5.
a = 20
b = bin(a)
h = hex(a)
o = oct(a)

print(b)
print(h)
print(o)

#6.
b = "10100"
i = int(b, 2)
print(i)

h = "14"
i = int(h, 16)
print(i)

o = "24"
i = int(o, 8)
print(i)



