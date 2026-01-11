#Mathematical Foundations

#Even / Odd

#Floor & Ceil

#Sum of first N natural number
#Sum = (n(n+1))/2
n = 7
print(1+2+3+4+5+6+7)
print((n * (n+1)) // 2)

#Decimal to binary
def binary(num):
    bits = []
    while num > 0:
        bits.append(str(num % 2))
        num = num // 2

    return ''.join(bits[::-1])

print(binary(48))
print(binary(0))

#Check if a larger number is divisible by 13 or not
def is_divisible_by_13_str(s):
    remainder = 0
    for digit in s:
        remainder = (remainder * 10 + int(digit)) % 13
    return remainder == 0

#Angle between hour and minute hand
#Example -> 3:15

def get_angle(h, m):
    minute_angle = m * 6                        #90
    hour_angle = (h * 30) + (m * 0.5)           #90 + 7.5
    angle = abs(hour_angle - minute_angle)      #7.5
    return (min(angle, 360-angle))

print(get_angle(3,15))

#GCD

#GCD of multiple numbers

#LCM

#Palindrome number

#Armstrong number

#Perfect number

#Factors

