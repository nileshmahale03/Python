#check if key exists
student_marks = {"Alice": 85, "Bob": 90, "Charlie": 78}
print("Alice" in student_marks) #True
print("David" in student_marks) #False

#Iterate over keys
for key in student_marks:
    print(key)

#Iterate over values
for value in student_marks.values():
    print(value)

my_dict = {"a": 1, "b": 2, "c": 3}

values = list(my_dict.values())

print(values) # Output: [1, 2, 3]

#Iterate over key-value pairs
for key, value in student_marks.items():
    print(key, value, end= " ")
print()

#len
print(len(student_marks))

#copy() vs direct assignment
original = {"Alice": 85, "Bob": 90}
copy_dict = original.copy()
reference = original
copy_dict["Charlie"] = 78
reference["Charlie"] = 79
print(original)    # Outputs: {'Alice': 85, 'Bob': 90}
print(copy_dict)   # Outputs: {'Alice': 85, 'Bob': 90, 'Charlie': 78}

#update() or |
dict1 = {"Alice": 85, "Bob": 90}
dict2 = {"Charlie": 78, "Bob": 95}
dict1.update(dict2)
print(dict1) # Outputs: {'Alice': 85, 'Bob': 95, 'Charlie': 78}

dict1 = {"Alice": 85, "Bob": 90}
dict2 = {"Charlie": 78, "Bob": 95}
merged = dict1 | dict2
print(merged) # Outputs: {'Alice': 85, 'Bob': 95, 'Charlie': 78}


