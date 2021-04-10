
"""
Dictionary:
1. Normal variable holds 1 value; dictionary holds collection of key-value pairs; all keys must be distinct but values may be repeated
2. {} - curly bracket
3. Unordered
4. Mutable
5. uses Hashing internally
6. Functions:
    1. dict[]            : returns value at specified index
    2. len()             : returns length of dictionary
       min()             : returns min value in dictionary
       max()             : returns max value in dictionary
       sum()             : returns sum of values in dictionary
    3. dict.reverse()    : 'dict' object has no attribute 'reverse'
    4. dict.sort()       : 'dict' object has no attribute 'sort'
    5. in                : operator returns bool stating if specified value present in dictionary or not
    6. dict[key] = value : add value with specified key
    7. dict[key]         : get value from dict with specified key
       dict.get(key)       returns None if key dosen't exists
    11. dict.pop(key)    : dict.pop()
        dict.popitem()     pop() will remove last value
    12. del dict[key]    : delete

"""
dict = {10:"abc", 20:"xyz", 30:"pqr"}

print(dict)
print(type(dict))
print(dict[10])

print(dict, len(dict), min(dict), max(dict), sum(dict))

dict[40] = "def"

print(dict)

print(dict[30], dict.get(30))

print(dict.get(50), dict.get(60, "Not Available"))

#dict.reverse()
#dict.sort()

print(20 in dict, 80 in dict)

dict.popitem()
print(dict)

dict.pop(10)
print(dict)

del dict[30]
print(dict)