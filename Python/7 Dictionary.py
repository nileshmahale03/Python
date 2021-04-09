
#Dictionary
"""
    1. Collection of key-value pair
    2. Unordered
    3. All keys must be distinct
    4. Values may be repeated
    5. Uses Hashing Internally
"""
d = {110: "abc", 101:"xyz", 105:"pqr"}

print(d)

print(type(d))

d = {}

print(d)

d["laptop"] = 40000
d["mobile"] = 15000
d["earphone"] = 1000

print(d)

print(d["mobile"])
print(d.get("mobile"))

#print(d["xbox"])
print(d.get("xbox"))
print(d.get("xbox", "NA"))

#####################################################################

d = {110: "abc", 101: "xyz", 105: "pqr", 106: "bcd"}
print(d)

d[101] = "wxy"
print(d)

d.pop(105)
print(d)

del d[106]
print(d)

d[108] = "cde"
print(d)
d.popitem()
print(d)

#Problem
"""
Given a dictionary, and a list of queries(keys), you have to find and print the value of each query from the dictionary if present else it prints "None".

Example 1:

Input:
dict = {1:"abc", 2: "cde", 3: "fgh"}
query = [2, 3, 4]
Output:
cde
fgh
None

"""
dict = {1:"abc", 2: "cde", 3: "fgh"}
query = [2, 3, 4]

print(dict.get(2))
print(dict.get(3))
print(dict.get(4))

for key in query:
    print(dict.get(key))

print("########################################################")
