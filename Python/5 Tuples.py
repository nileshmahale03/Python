
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

#Problem:
"""
Given a tuple A , find if all elements of tuple are different or not.

Example 1:

Input:
A = (1, 2, 3, 4, 5, 4)
Output: 
Not Distinct
Example 2:

Input:
A = (1, 2, 3, 4, 5)
Output: 
Distinct

"""
A = (1, 2, 3, 4)

s = set(A)
if len(A) != len(s):
    output = "Not Distinct"
elif len(A) == len(s):
    output = "Distinct"

print(output)
print("#######################################################")

#Problem:
"""
Given a tuple A with distinct elements and an integer X, find the index position of X. Assume to have X in the tuple always.

Example 1:

Input:
A = (1, 2, 3, 4, 5)
X = 3
Output: 
2
Example 2:

Input:
A = (3, 2, 1, 5, 4)
X = 5
Output: 
3

"""

A = (1, 2, 3, 4, 5)
X = 3

for i in range(len(A)):
    if A[i] == X:
        print(i)
