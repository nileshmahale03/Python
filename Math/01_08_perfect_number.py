#Perfect number
#A number is called a perfect number if it is equal to the sum of its proper divisors
#Example: 6 → divisors: 1, 2, 3 → sum = 6
def is_perfect(num):
    total = 1        # 1 is always a proper divisor
    i = 2

    while i * i <= num:
        if num % i == 0:
            total += i
            if i != num // i:
                total += num // i
        i += 1

    return total == num

print(is_perfect(6), is_perfect(18))