#keys(), values(). items()

student_marks = {"Nilesh": 90, "Nishiv": 100, "Madhuri": 95}
print(student_marks.keys())
print(student_marks.values())
print(student_marks.items())

#pop(), popitem()

#get(), setdefault()

#fromkeys()
keys = ["Alice", "Bob", "Charlie"]
new_dict = dict.fromkeys(keys, 0)
print(new_dict)