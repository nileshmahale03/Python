#Functions
def greet():
    print("Hello, world!")

greet()  # This will print "Hello, world!"

#Parameters
def greet(name):
    msg = "Hello, " + name
    print(msg)

greet("Alice")  # This will print "Hello, Alice"

#Multiple Parameters
def greet(name, greeting):
    message = greeting + " " + name
    print(message)

greet("Alice", "Hello")  # This will print "Hello Alice"

#Return Statement
def add(x, y):
    return x + y

result = add(3, 5)
print(result)  # This will print 8

#Type Hints
def add(x: int, y: int) -> int:
    return x + y

result = add(3, 5)
print(result)  # This will print 8

#Default Arguments
def greet(name="world"):
    print("Hello, " + name + "!")

greet()       # This will print "Hello, world!"
greet("Bob")  # This will print "Hello, Bob!"

