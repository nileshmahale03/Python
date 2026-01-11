#break => terminate and exit the loop immediately 
#continue => skip current iteration and moves to next iteration
#pass => Acts as a placeholder and does nothing. We cannot have empty loops, so we use pass to avoid errors

#1-Print 1 to 10- stop if mutiple of 6
counter = 0

while (counter < 10):
    counter += 1
    if (counter % 6 == 0):
        break
    print(counter)


#2-Print 1 to 10- skip mutiples of 3
counter = 0

while (counter < 10):
    counter += 1
    if (counter % 3 == 0):
        continue
    print(counter)



