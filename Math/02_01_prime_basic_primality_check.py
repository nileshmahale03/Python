#prime number
#A prime number is a natural number greater than 1 that has exactly two distinct positive divisors — 1 and itself.

#Basic Primality Check
#To check if a number n is prime, try dividing it by numbers from 2 to n-1. 
#If any number divides it, then n is not prime; otherwise, it is.

def is_prime(num):
    for i in range(2, num):
        print(i)
        if num % i == 0:
            return False
    return True

print(is_prime(101))