
#Set
"""
    1. Distinct Elements
    2. Unordered
    3. No Indexing
    4. Union, Intersection, Except
    5. Uses Hashing Internally
"""

s = {10, 20, 30}

print(type(s))

print(s)

#add
s.add(40)

print(s)

s.add(40) #adding duplicate item

print(s)

#update
s.update([50, 60])

print(s)

s.update([70, 80], [90, 100])

print(s)

#discard
s.discard(100)

print(s)

#remove
s.remove(90)

print(s)

#clear
s.clear()

print(s)

#del
s.add(10)

print(s)

del s

#len
s = {1 ,3 , 5, 7}

print(len(s))

#in
print(3 in s)

print(9 in s)

########################################################

s1 = {2, 4, 6, 8}
s2 = {3, 6, 9}
#union
print(s1 | s2)

#intersection
print(s1 & s2)

#except or difference
print(s1 - s2)
print(s2 - s1)

#symmetric_difference
print(s1 ^ s2)
########################################################

s1 = {2 ,4, 6, 8}
s2 = {4, 8}
#isdisjoint: Two sets are said to be disjoint sets if they have no common elements.
print(s1.isdisjoint(s2))

#issubset
print(s1 <= s2)

#issuperset
print(s1 >= s2)
