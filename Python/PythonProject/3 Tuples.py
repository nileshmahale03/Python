
"""
Tuple:
1. Normal variable holds 1 value; Tuple holds collection of values
2. () - small bracket
3. Ordered
4. Immutable
5. has index
6. Functions:
    1. t[]         : returns value at specified index
    2. len()       : returns length of tuple
       min()       : returns min value in tuple
       max()       : returns max value in tuple
       sum()       : returns sum of values in tuple
    3. t.reverse() : 'tuple' object has no attribute 'reverse'
    4. t.sort()    : 'tuple' object has no attribute 'sort'
    5. in          : operator returns bool stating if specified value present in tuple or not
    6. t.append()  : 'tuple' object has no attribute 'append'
    7. t.insert()  : 'tuple' object has no attribute 'insert'
    8. t.count()   : count occurence of specified value
    9. t.index()   : returns index of specified value
    10. t.remove() : 'tuple' object has no attribute 'remove'
    11. t.pop()    : 'tuple' object has no attribute 'pop'
    12. del t[]    : 'tuple' object doesn't support item deletion
"""

t = (10, 20, 20, 40, 50)
#    0,  1,  2,  3,  4
#   -5, -4, -3, -2, -1

print(t)
print(type(t))
print(t[2])
print(t[-1])

print(t, len(t), min(t), max(t), sum(t))

#t.reverse()

#t.sort()

print(20 in t, 80 in t)

#t.append(60)

#t.insert(2, 20)

print(t.count(20))

print(t.index(20))
print(t.index(20, 2, 7))

#t.remove(20)

#t.pop()

#del t[2]


