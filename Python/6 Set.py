
#Set
"""
    1. Distinct Elements
    2. Unordered
    3. No Indexing
    4. Union, Intersection, Except
    5. Uses Hashing Internally

A set is an unordered collection of items where every element is unique and must be immutable, but set is mutable. You cannot access an element of set using indexing or slicing, but you can update the set.

Some important functions in Set in Python:
add()     : Adds an element to the set.
clear()   : Removes all elements from the set
discard() : Removes an element from the set if present.
remove()  : Removes an element from the set. If the element is not present, it raises error.
pop()     : Removes and returns an arbitary set element. Raise error if the set is empty.
union()   : Returns the union of sets in a new set
update()  : Updates the set with the union of itself and others
len()     : Return the length of set.
sorted()  : Return a new sorted list from elements in the set.
sum()     : Return the sum of all elements in the set.
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


############################################################

S = {1, 3, 5, 7}
print(sum(s))
