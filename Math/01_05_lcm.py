#LCM
#The LCM (Least Common Multiple) is the smallest number that is divisible by both a and b.
#Formula: lcm(a,b)= (a * b)/ gcd(a,b)
def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a

print((48 * 18) // gcd(48, 18))