#for
#iterate over a sequence (like a list, string, range)

for i in range(5):
    print(i)

word = "artifical intelligence"

#Example 1 - Looping over a string
for w in word:
    print(w)

#Example 2 - Check if char 'i' exists in word
if 'i' in word:
    print("i letter exists")

#Example 3 - Count number of i's in the word
count = 0
for w in word:
    if w == 'i':
        count += 1
print(count)

#Nested Loop
for i in range(1, 3):
    for j in range(1, 3):
        print(i, j)


