#split()
s = "hello world python"
print(s.split())         #['hello', 'world', 'python']

#capitalize()
text = "hello, python!"
print(text.capitalize())  # Outputs: Hello, python!

#title()
text = "python programming is fun"
print(text.title())  # Outputs: Python Programming Is Fun

#swapcase()
text = "Hello, Python!"
print(text.swapcase())  # Outputs: hELLO, pYTHON!

#zfill(width)
text = "42"
print(text.zfill(5))  # Outputs: 00042

#Alignment Methods
text = "Python"
print(text.ljust(10, "-"))  # Outputs: Python----
print(text.rjust(10, "*"))  # Outputs: ****Python
print(text.center(10, "="))  # Outputs: ==Python==

#isalnum()
text = "Python3"
print(text.isalnum())  # Outputs: True

#isalpha()
text = "Python"
print(text.isalpha())  # Outputs: True

#isdigit()
text = "12345"
print(text.isdigit())  # Outputs: True

#islower()
text = "python"
print(text.islower())  # Outputs: True

#isupper()
text = "PYTHON"
print(text.isupper())  # Outputs: True

#isspace()
text = "   "
print(text.isspace())  # Outputs: True

#partition(substring)
#Splits the string into three parts: before the substring, the substring itself, and after the substring.
text = "Hello, Python World!"
print(text.partition("Python"))  
# Outputs: ('Hello, ', 'Python', ' World!')

#rpartition(substring)
#Similar to partition(), but starts splitting from the right.
text = "Hello, Python Python!"
print(text.rpartition("Python"))  
# Outputs: ('Hello, Python ', 'Python', '!')

#.replace()
#new_string = old_string.replace(old, new)