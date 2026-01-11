#Segmented Sieve
#find prime numbers between a = 10, b = 30
#Compute primes up to √30 ≈ 5 → [2, 3, 5]
#Mark multiples of these inside [10, 30]
#Remaining numbers are primes
def simple_sieve(limit):
    prime = [True] * (limit + 1)
    prime[0] = prime[1] = False

    for i in range(2, int(limit ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, limit + 1, i):
                prime[j] = False

    return [i for i in range(2, limit + 1) if prime[i]]


def segmented_sieve(a, b):
    limit = int(b ** 0.5) + 1
    base_primes = simple_sieve(limit)

    is_prime = [True] * (b - a + 1)

    for p in base_primes:
        # first multiple of p in [a, b]
        start = max(p * p, ((a + p - 1) // p) * p)

        for multiple in range(start, b + 1, p):
            is_prime[multiple - a] = False

    # handle a = 0 or 1
    if a == 0:
        is_prime[0] = False
    if a <= 1:
        is_prime[1 - a] = False

    return [a + i for i in range(b - a + 1) if is_prime[i]]