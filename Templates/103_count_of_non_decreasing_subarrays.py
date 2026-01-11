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