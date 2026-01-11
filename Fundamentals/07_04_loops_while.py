#while
#repeat while a condition is True
#start with 0 or 5 
#don't use <= or >= 

#Example 1 - print 1 to 5
counter = 0
while counter < 5:
    counter += 1
    print(counter)

#Example 2 - print 5 to 1
counter = 5
while counter > 0:
    print(counter)
    counter -= 1

#Example 3 - Infinite Loop
while True:
    print("Prime")