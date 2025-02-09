#Input
 
#input() function
 
user_input = input() # This will read one line of input from stdin
print(user_input) # This will print the input to the console
 
#If you're expecting a different type of input like an integer or a float,
#you need to explicitly convert it using int() or float().
 
age = int(input())
temperature = float(input())
print(age, temperature)
 
#split() method
 
name, age = input().split()
print(name, age)
 
info = input().split()
print(info)
 
#map
 
arr = list(map(int, input().split()))
print(arr)