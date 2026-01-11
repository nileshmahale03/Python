#generate all subarrays 
#formula -> (N * (N+1))/2
#Continuous -> Yes
N = 4
A = [1, 6, 3, 7]

for i in range(N):
    for j in range(i, N):
        print(A[i:j+1])