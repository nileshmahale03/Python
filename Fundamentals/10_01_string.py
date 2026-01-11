#string
#sequence of characters
#immutable

str1 = "hello world"
str2 = "prime"

print(len(str1)) #11

#concatenation

word = str1 + " " + str2
print(word)      #"hello world prime"

#loops
for w in word:
    print(w)

for i in range(len(word)):
    print(i, word[i])

for idx, val in enumerate(word):
    print(idx, val)

#indexing
print(word[0])   #h
print(word[3])   #l
print(word[-1])  #e

#slicing
#Slicing allows us to extract a substring from a string
#string[start: stop: step]

s = "Python"
print(s[0:2])    #Py
print(s[2:])     #thon
print(s[:3])     #Pyt
print(s[::2])    #Pto
print(s[::-1])   #nohtyP

#remove 4th character
word = "Nilesh Mahale"
word = word[:3] + word[4:]
print(word)

#string formatting
name = "Nilesh"
age = 39
text = f"My name is {name} and I am {age} years old"
print(text)

#sort
s = "dcba"
s.sort()   # ❌ ERROR #Strings in Python are immutable, so this will ❌ NOT work:
sorted_chars = sorted(s)
print(sorted_chars)
result = ''.join(sorted_chars)
print(result)

#reverse characters from index l to r
s = "abcdef"
l = 1
r = 4

s = s[:l] + s[l:r+1][::-1] + s[r+1:]
print(s) #aedcbf

#Repetition
text = "Python! "
result = text * 3
print(result)  # Outputs: Python! Python! Python!

#Comparison
#Comparisons are case-sensitive and performed lexicographically.
text1 = "apple"
text2 = "banana"
print(text1 < text2)  # Outputs: True (because 'a' comes before 'b')

