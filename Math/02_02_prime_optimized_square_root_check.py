#Optimized Method (Square Root Check):
#We only need to check up to √n because if n has a factor larger than √n, the corresponding smaller factor must be less than √n.
#So if no number from 2 to √n divides n, then n is prime.

def is_prime(num):
    for i in range(2, int(num ** 0.5)+1):
        print(i)
        if num % i == 0:
            return False
    return True

print(is_prime(101))