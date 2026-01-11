#prime factors
#basic
def prime_factors(n):
    ret = []
    i = 2
    while i <= n:
        print(i)
        while n % i == 0:
            ret.append(i)
            n //= i
        i += 1
    return ret
print(prime_factors(670))

#optimized - square root check
def factor(n):
    ret = []
    i = 2
    while i * i <= n:
        print(i)
        while n % i == 0:
            ret.append(i)
            n //= i
        i += 1
    if n > 1:
        ret.append(n)
    return ret

print(factor(670))

#SPF
def compute_spf(n):
    spf = list(range(n + 1))

    for i in range(2, int(n ** 0.5) + 1):
        if spf[i] == i:          # i is prime
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf

def prime_factors(n, spf):
    factors = []
    while n > 1:
        factors.append(spf[n])
        n //= spf[n]
    return factors

MAXN = 100
spf = compute_spf(MAXN)

print(prime_factors(84, spf))    # [2, 2, 3, 7]
print(prime_factors(100, spf))   # [2, 2, 5, 5]
print(prime_factors(97, spf))    # [97]