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