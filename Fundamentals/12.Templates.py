#1. Count occurence of element in list
A = [1, 2, 3, 1, 2, 4, 1, 3, 5]

A_freq = {}
for item in A:
    if item in A_freq:
        A_freq[item] += 1
    else:
        A_freq[item] = 1

print(A_freq)

#2. Count digits in a number
#. Number of times you can divide a number by 10
num = 27362736
count = 0
while num != 0:
    count = count + 1
    num = num // 10
print(count)

#3. Prime Number
n = 13
isPrime = True # Assume n is prime
i = 2
while i < n:
    if n % i == 0:
        isPrime = False
        break
    i += 1

print("Yes" if isPrime else "No")

#4. Factorial of a Number
n = 5
i = 1
factorial = 1
while i <= n:
    # We need to multiply by i in each iteration
    factorial = i * factorial
    i = i + 1
    
print("The factorial of the given number is:", factorial)

#5. Fibonacci series
#A Fibonacci number is a series of numbers in which each number is obtained by adding the two preceding numbers.
n = 8
a = 0
b = 1
print(a, b, end=" ")
for i in range(n-2):
    c = a+b # set currrent number as sum of previous two numbers
    print(c, end=" ")
    # Update a and b as next two numbers
    a = b 
    b = c