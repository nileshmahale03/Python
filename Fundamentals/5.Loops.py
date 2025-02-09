#Loops
#It's like telling the computer, "Keep doing this until I say stop!"
#When using a while loop you have to think about three things - initialisation, condition and update statement.
#FOR loop in Python is designed to iterate over a sequence of elements, such as a list, string, or range of numbers.

#while loop
print("while loop")
i = 0 
while i < 10:
    print(i)
    i += 1

#for loop
print("for loop")
for i in range(10):
    print(i)

print("while loop: start")
i = 2
while i < 5:
    print(i)
    i += 1

print("for loop: start")
for i in range(2, 5):
    print(i)

print("while loop: range")
i = 0
while i < 10:
    print(i)
    i += 2

print("for loop: range")
for i in range(0, 10, 2):
    print(i)

print("while loop: reverse")
i = 9
while i > -1:
    print(i)
    i -= 1

print("for loop: reverse")
for i in range(9, -1, -1):
    print(i)

#Nested Loop
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

#Control Flow

'''
break    : Exits the loop immediately.
continue : Skips the remaining code inside the loop for the current iteration and moves to the next iteration.
pass     : Acts as a placeholder and does nothing. We cannot have empty loops, so we use pass to avoid errors. It can also be used in conditional statements and functions.
'''

print("Control Flow")
for i in range(1, 8):
    if i == 3:
        continue  
    elif i == 6 :
        break  
    print(i)

def unfinsished_function():
    pass