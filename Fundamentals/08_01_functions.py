#functions
def avg(a, b, c):
    return (a + b + c) / 3

print(avg(1, 2, 3))

#Parameters - single
def greet(name):
    print("Hello, " + name) #print("Hello, " + name) vs print("Hello, " , name)

greet("nilesh") #When calling a function, you can pass values, variables, or expressions as arguments to the function.

#Parameters - multiple
def greet(name, message):
    print(message, name)

greet("nilesh", "Hi")

#Return Statement
#This allows you to use the result of a function in other parts of your code, outside of the original function.
#Once a return statement is executed, the function will stop executing.
def add(a , b):
    return a + b

result = add(3 , 5)
print(result)

#Type Hints
#you can add type hints to your functions to indicate what type of data the function expects to receive and return
#This is not required, but it can be helpful for other developers who are reading your code.
def greet(name: str) -> None:
    print("Hello, " + name)

greet("nilesh")

def add(a: int , b: int) -> int:
    return a + b

result = add(3 , 5)
print(result)

from typing import List, Dict, Tuple, Set # used to add type hint for List

#Default Arguments
#If you have a parameter with a default value, all parameters after it must also have default values.
def greet(message="Hello", name="World!"):
    print(message, name)

greet("Hey", "Nilesh")
greet()

#lambada function
average = lambda a, b, c: (a + b + c) / 3
print(average(1, 2, 3))