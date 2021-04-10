
"""
Set:
1. Normal variable holds 1 value; set holds collection of distinct values
2. {} - curly bracket
3. Unordered
4. Mutable
5. No index
6. Functions:
    1. s[]          : 'set' object is not subscriptable
    2. len()        : returns length of set
       min()        : returns min value in set
       max()        : returns max value in set
       sum()        : returns sum of values in set
    3. s.reverse()  : 'set' object has no attribute 'reverse'
    4. s.sort()     : 'set' object has no attribute 'sort'
    5. in           : operator returns bool stating if specified value present in set or not
    6. s.add()      : adds value in the set
       s.update([]) : adds list items to the set
    7. s.insert()   : 'set' object has no attribute 'insert'
    8. s.count()    : 'set' object has no attribute 'count'
    9. s.index()    : 'set' object has no attribute 'index'
    10. s.remove()  : removes specified value
        s.discard() : discard specified value
        s.clear()   : clears entire set
    11. s.pop()     : pop() will remove last value; set.pop() takes no arguments
    12. del s       : delete set
7. Uses Hashing internally
8. Set Functions:
    1. .union
    2. .intersection
    3. .difference
    4. .symmetric_difference
    5. .isdisjoint
    6. .issubset
    7. .issuperset
"""

s = {10, 20, 30, 40, 50}
#    0,  1,  2,  3,  4
#   -5, -4, -3, -2, -1

print(s)
print(type(s))
#print(s[2])
#print(s[-1])

print(s, len(s), min(s), max(s), sum(s))

#s.reverse()

#s.sort()

print(20 in s, 80 in s)

s.add(60)
print(s)

s.update([70])
print(s)

s.update([80, 90])
print(s)

#s.insert(2, 20)

#print(s.count(20))

#print(s.index(20))
#print(s.index(20, 2, 7))

s.remove(20)
print(s)

s.discard(60)
print(s)

s.clear()
print(s)

s = {10, 20, 30, 40, 50}

s.pop()
print(s)

#s.pop(-3)

del s

set1 = {2, 4, 6, 8}
set2 = {3, 6, 9}
set3 = {4, 8}

print(set1.union(set2))
print(set1 | set2)

print(set1.intersection(set2))
print(set1 & set2)

print(set1.difference(set2))
print(set1 - set2)

print(set1.symmetric_difference(set2))
print(set1 ^ set2)

print(set1.isdisjoint(set2))

print(set1.issubset(set3))

print(set1.issuperset(set3))
