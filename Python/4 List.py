
#List
#Normal variable holds 1 value, lists holds collection of values
#Square Brackets
#Mutable

"""
    l[]
    l[-]
    .append
    .insert
    in
    .count
    .index
    .remove
    .pop
    del
    max
    min
    sum
    .reverse
    .sort
"""

l = [10, 20, 30, 40, 50]
#     0,  1,  2,  3,  4
#    -5, -4, -3, -2, -1

print(type(l))

print(l)

print(l[3])

print(l[-1])  #get last item

print(l[-2])  #get 2nd last item

#append
l.append(30)

print(l)

#insert
l.insert(1, 15)

print(l)

#in
print(20 in l)
print(25 in l)

#count
print(l.count(30))

#index
print(l.index(30))

print(l.index(30, 4, 7))

#remove
l.remove(20)

print(l)

#pop
l.pop()

print(l)

l.pop(2)

print(l)

#del
del l[1]

print(l)

del l[0:2]

print(l)

#max
l = [10, 40, 20, 50]

print(l)

print(max(l))

#min
print(min(l))

#sum
print(sum(l))

#reverse
l.reverse()

print(l)

#sort
l.sort()

print(l)