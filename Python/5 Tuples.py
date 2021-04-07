
#Tuple
#ordered
#indexed
#Immutable
#Faster than list

t = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

print(t)

print(type(t))

#t.append(20) AttributeError: 'tuple' object has no attribute 'append'

print(t[2])
print(t[-1])
print(t[1:3])

print(len(t))

print(t.count("Monday"))

print(t.index("Friday"))