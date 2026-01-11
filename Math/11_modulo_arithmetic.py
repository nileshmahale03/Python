
#modulo arithmetic
#a%b = a - (b * ⌊a/b⌋)

print(8 % 3)    #2
print(8 % -3)   #-1
print(-8 % 3)   #1
print(-8 % -3)  #-2

print(-8/3), print(-8-(-9))

#10^9+7

a = 7
b = 5
m = 3

#Addition
ans = (a + b) % m = (a % m + b % m) % m
print(ans)

#Subtraction
ans = (a - b) % m = (a % m - b % m) % m
print(ans)

#Multiplication
ans = (a * b) % m = ((a % m) * (b % m)) % m
print(ans)

#Exponentiation
ans = (a ** b) % m = ((a % m) ** b) % m
ans = pow(a, b, m)
print(ans)

#Division
import math
def modDivide(a, b, M):
	if math.gcd(b, M) != 1:
		return -1
	
	return (a * pow(b, -1, M)) % M

#Modular Inverse
inv = pow(a, m-2, m)

#Fermat Reduction
'''
Compute 3^100 mod 7
	•	7 is prime → reduce exponent mod 6
	•	100 mod 6 = 4
	•	3^4 mod 7 = 81 mod 7 = 4
'''

#fast Exp
