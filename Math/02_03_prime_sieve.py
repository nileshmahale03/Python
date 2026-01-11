#Sieve of Eratosthenes
#The Sieve of Eratosthenes efficiently finds all primes up to n by repeatedly marking multiples of each prime as non-prime, starting from 2. 
#This avoids redundant checks and quickly filters out all composite numbers.

def sieve(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    
    for p in range(2, int(n ** 0.5) + 1):
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
    
    res = [i for i in range(2, n+1) if prime[i]]

    return res

print(sieve(100))