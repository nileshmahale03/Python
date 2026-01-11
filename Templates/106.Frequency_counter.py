#Counter
from collections import Counter
A = [1, 2, 3, 4, 5, 3, 2, 1, 5, 3]

freq = Counter(A)

for key in sorted(freq):
    print(key, freq[key])

#frequency dict
word = "hello"

my_dict = {}
for w in word:
    if w in my_dict:
        my_dict[w] += 1
    else:
        my_dict[w] = 1

print(my_dict)