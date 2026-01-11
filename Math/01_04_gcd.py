#GCD
#The GCD (Greatest Common Divisor) of two numbers a and b is the largest number that divides both
#Euclidean algorithm: gcd(a,b) = gcd(b,a%b), Stops when b = 0
def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a

print(gcd(48, 18)) #6

#GCD of multiple numbers
import math
from functools import reduce

nums = [2, 2, 6, 8, 12]
gcd_all = reduce(math.gcd, nums)

print(gcd_all)

'''
Linear Diophantine Equation Theorem
The equation: Ax + By = C has an integer solution if and only if:
C is divisible by gcd(A, B)

That’s it. No need to actually find x or y.
'''