'''

5. Bitwise Operators: Perform operations at the binary level (&, |, ^, ~, <<, >>).

'''

a = 5  # Binary: 0101
b = 3  # Binary: 0011

print(a & b)  # Output: 1 (Binary: 0001)           #returns 1 if both bits are 1
print(a | b)  # Output: 7 (Binary: 0111)           #returns 1 if at least one bit is 1
print(a ^ b)  # Output: 6 (Binary: 0110)           #returns 1 if the bits are different
print(~a)     # Output: -6 (Binary: -(0101 + 1))   #inverts all bits, flipping 0 to 1 and 1 to 0
print(a << 1) # Output: 10 (Binary: 1010)          #Each shift effectively multiplies the number by 2
print(a >> 1) # Output: 2 (Binary: 0010)           #Each shift effectively divides the number by 2 and discards the remainder

