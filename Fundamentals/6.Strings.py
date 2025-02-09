#len Function
my_str = "NeetCode"
print(len(my_str))  # Output: 8

#String Indexing (Positive and Negative)
my_str = "Hello" 
#  Hello
#  01234
#  -5-4-3-2-1
print(my_str[0])   # Output: H
print(my_str[1])   # Output: e
print(my_str[2])   # Output: l
print(my_str[3])   # Output: l
print(my_str[4])   # Output: o
print(my_str[-1])  # Output: o

#String Looping
my_string = "Hello, World!"
#1
for i in range(len(my_string)):
    print(i, my_string[i])
#2
for char in my_string:
    print(char)

#String Concatenation
str1 = "Hello, "
str2 = "world!"
print(str1 + str2) # Output: Hello, world!

#String Repetition
print(str1 * 3)

#String Slicing
#substring = string[start:end]
#substring = string[start:end:step]
my_string = "NeetCode"

print(my_string[4:8]) # Output: Code
print(my_string[4:])  # Output: Code

print(my_string[0:3]) # Output: Nee
print(my_string[:3])  # Output: Nee

#Reversing a String
my_string = "Hello"

print(my_string[::-1])  # Output: olleH

#Strings are Immutable
message = "I will never change."

before_second = message[:1] # "I"
after_second = message[2:]  # "will never change."
new_message = before_second + after_second
print(new_message)

#String Formatting
name = "Alice"
age = 25

msg = "Hello, {}. You are {} years old.".format(name, age)
print(msg)  # Output: Hello, Alice. You are 25 years old.

#String functions
name = "CodeChef"
lowercase_name = name.lower()
uppercase_name = name.upper()
print(lowercase_name, uppercase_name)

name = "Chaf"
new_name = name.replace("a", "e")
print(new_name)




