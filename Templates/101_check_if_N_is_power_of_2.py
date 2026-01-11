#A number N is a power of 2 if and only if N & (N - 1) == 0 and N > 0
N = int(input())

if N > 0 and (N & (N - 1)) == 0:
    print("YES")
else:
    print("NO")