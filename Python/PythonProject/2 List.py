
"""
List:
1. Normal variable holds 1 value; lists holds collection of values
2. [] - Square bracket
3. Ordered
4. Mutable
5. has index
6. Functions:
    1. l[]         : returns value at specified index
    2. len()       : returns length of list
       min()       : returns min value in list
       max()       : returns max value in list
       sum()       : returns sum of values in list
    3. l.reverse() : reverse the list
    4. l.sort()    : sort the list in asc order
    5. in          : operator returns bool stating if specified value present in list or not
    6. l.append()  : appends value at the end
    7. l.insert()  : inserts value at the specified index
    8. l.count()   : count occurence of specified value
    9. l.index()   : returns index of specified value
    10. l.remove()  : removes 1st occurence of specified value
    11. l.pop()    : removes value at specified index; pop() will remove value at last index
    12. del l[]    : delete list at specified index or range of index
"""

l = [10, 20, 30, 40, 50]
#    0,  1,  2,  3,  4
#   -5, -4, -3, -2, -1

print(l)
print(type(l))
print(l[2])
print(l[-1])

print(l, len(l), min(l), max(l), sum(l))

l.reverse()
print(l)

l.sort()
print(l)

print(20 in l, 80 in l)

l.append(60)
print(l)

l.insert(2, 20)
print(l)

print(l.count(20))

print(l.index(20))
print(l.index(20, 2, 7))

l.remove(20)
print(l)

l.pop()
print(l)

l.pop(-3)
print(l)

del l[2]
print(l)

del l[1: 3]
print(l)

