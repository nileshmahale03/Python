#Frequency Array
A = [1, 2, 3, 4, 5, 3, 2, 1, 5, 3]

freq = [0] * (len(A) + 1)

for value in A:
    freq[value] += 1

for i in range(1, len(freq)):
    print(freq[i], end=" ")