
#id function

x = 10

print(id(x))  #140607028914768

y = 20

print(id(y))  #140607028915088

z = y

print(id(z))  #140607028915088

#is operator gives you a Boolean value

print(y is z)

print(x is z)