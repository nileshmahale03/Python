#dictionary
#key-value pairs (unique keys)
#unordered
#mutable
#dynamic

#syntax
'''
dictionary_name = {
    key1: value1,
    key2: value2,
    key3: value3
}
'''
#1. create dictionary
#Using Curly Braces {}
student_marks = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}
print(student_marks) # Outputs: {'Alice': 85, 'Bob': 90, 'Charlie': 78}

#Using the dict() Constructor
student_marks = dict(Alice=85, Bob=90, Charlie=78)
print(student_marks)

#Empty dictionary
empty_dict = {}
print(empty_dict)

#2. Accessing Dictionary Elements
print(student_marks["Alice"]) #85
print(student_marks.get("Bob")) #90

#3. Adding and Updating Dictionary Elements
student_marks["Nilesh"] = 99
print(student_marks)

student_marks["Nilesh"] = 100
print(student_marks)

#4. Deleting Dictionary Elements
#del
del student_marks["Charlie"]
print(student_marks)

#pop()
removed_value = student_marks.pop("Nilesh")
print(removed_value, student_marks)

#clear()
student_marks.clear()
print(student_marks)