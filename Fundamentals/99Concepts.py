
negative_infinity = float('-inf')
positive_infinity = float('inf')

#A number N is a power of 2 if and only if N & (N - 1) == 0 and N > 0
N = int(input())

if N > 0 and (N & (N - 1)) == 0:
    print("YES")
else:
    print("NO")

#generate all subarrays 
#formula -> (N * (N+1))/2
#Continuous -> Yes
N = 4
A = [1, 6, 3, 7]

for i in range(N):
    for j in range(i, N):
        print(A[i:j+1])

#Number of non-decreasing subarrays
'''
Idea
	•	Traverse array once
	•	Keep track of current non-decreasing streak length
	•	When the streak breaks, add its contribution
'''
N = int(input())
A = list(map(int, input().split()))

nums = []
count = 1
for i in range(1, N):
    if A[i] >= A[i - 1]:
        count += 1
    else:
        nums.append(count)
        count = 1
nums.append(count)

ans = 0
for n in nums:
    ans += (n * (n + 1)) // 2

print(ans)

#genaret all subsequence 
#formula -> (2 ** N)
#Continuous -> No
def generate_subsequence(idx, path):
    if idx == len(A):
        print(path)
        return
    
    #Not Take
    generate_subsequence(idx + 1, path) 

    #Take
    path.append(A[idx])
    generate_subsequence(idx + 1, path)
    path.pop()

A = [1, 6, 3, 7]
generate_subsequence(0, [])

#Frequency Array
A = [1, 2, 3, 4, 5, 3, 2, 1, 5, 3]

freq = [0] * (len(A) + 1)

for value in A:
    freq[value] += 1

for i in range(1, len(freq)):
    print(freq[i], end=" ")

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

#merge two strings alternately
N = int(input())

for _ in range(N):
    S, T = input().split()
    ans = ''

    min_len = min(len(S), len(T))

    for i in range(min_len):
        ans += S[i] + T[i]

    ans += S[min_len:]
    ans += T[min_len:]

    print(ans)