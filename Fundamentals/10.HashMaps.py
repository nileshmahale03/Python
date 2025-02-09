#Dictionaries/maps/hashmaps

'''
1. The keys within a dictionary must be unique, but the values can be duplicated.
2. A dictonary is like a table with two columns. The first column is the key, and the second column is the value.
3. A dictonary can be created using curly braces {}
'''

#Creating a dictionary
my_dict = {}

my_dict["Alice"] = 25
my_dict["Bob"] = 30
my_dict["Charlie"] = 35

print(my_dict)  # Output: {'Alice': 25, 'Bob': 30, 'Charlie': 35}

my_dict = {"Alice": 25, "Bob": 30, "Charlie": 35}

print(my_dict)

#Dict Operations
#Adding items to a dictionary - To add a new key-value pair to a dictionary, you simply assign a value to a new key.
my_dict = {"name": "Alice", "age": 30}
my_dict["location"] = "New York"

#To modify an existing value associated with a key in a dictionary, you can simply reassign a new value to that key.
my_dict = {"name": "Alice", "age": 30}
my_dict["age"] = 31  # Update the value for the key "age"

#in keyword
#To check if a dictionary contains a key, you can use the in keyword.
my_dict = {"a": 1, "b": 2, "c": 3}

print("a" in my_dict) # Output: True
print("d" in my_dict) # Output: False

#get(): Allows you to retrieve the value for a given key if it exists.
my_dict = {"name": "Alice", "age": 30}
print(my_dict.get("name"))  # Output: Alice
print(my_dict.get("location"))  # Output: None

#To check if a dictionary contains a value, you can use the in keyword.
my_dict = {"a": 1, "b": 2, "c": 3}

print(1 in my_dict.values()) # Output: True
print(5 in my_dict.values()) # Output: False

#Dict Looping
#Iterating Over Keys:
my_dict = {"name": "Alice", "age": 30, "location": "New York"}
for key in my_dict:
    print("Key:", key)

#Iterating Over Values:
my_dict = {"name": "Alice", "age": 30, "location": "New York"}
for value in my_dict.values():
    print("Value:", value)

#Iterating Over Key-Value Pairs:
my_dict = {"name": "Alice", "age": 30, "location": "New York"}
for key, value in my_dict.items():
    print("Key:", key, ", Value:", value)

#4
my_dict = {"a": 1, "b": 2, "c": 3}

values = list(my_dict.values())
print(values) # Output: [1, 2, 3]

#Dict Remove
#del: Allows you to remove a specific key-value pair from the dictionary.
my_dict = {"name": "Alice", "age": 30}
del my_dict["age"]  # Remove the key "age" and its corresponding value

#pop(): Removes a specified key and returns the corresponding value.
my_dict = {"name": "Alice", "age": 30}
removed_age = my_dict.pop("age")  # Remove the key "age" and retrieve its value

#clear(): Removes all key-value pairs from the dictionary, leaving it empty.
my_dict = {"name": "Alice", "age": 30}
my_dict.clear()  # Clear all key-value pairs


