students = {
    "Alice": {"age": 20, "grade": "A"},
    "Bob": {"age": 22, "grade": "B"},
    "Charlie": {"age": 21, "grade": "A"}
}
print(students)
# Outputs: {'Alice': {'age': 20, 'grade': 'A'}, 'Bob': {'age': 22, 'grade': 'B'}, 'Charlie': {'age': 21, 'grade': 'A'}}

print(students["Alice"])  # Outputs: {'age': 20, 'grade': 'A'}

print(students["Alice"]["age"])  # Outputs: 20

students["David"] = {"age": 23, "grade": "B"}
print(students)
# Outputs: {'Alice': {...}, 'Bob': {...}, 'Charlie': {...}, 'David': {'age': 23, 'grade': 'B'}}

students["Alice"]["grade"] = "A+"
print(students["Alice"])
# Outputs: {'age': 20, 'grade': 'A+'}

del students["Bob"]
print(students)
# Outputs: {'Alice': {...}, 'Charlie': {...}, 'David': {...}}

students["Alice"].pop("grade")
print(students["Alice"])
# Outputs: {'age': 20}

for student in students:
    print(student)
# Outputs: Alice, Charlie, David

for student, details in students.items():
    print(f"{student}'s details:")
    for key, value in details.items():
        print(f"  {key}: {value}")
# Outputs:
# Alice's details:
#   age: 20
#   grade: A+
# ...

