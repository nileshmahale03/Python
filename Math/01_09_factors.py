#factors
#To find factors of a number n, iterate from 1 to √n and check n % i == 0. Store both i and n/i
def factors(num):
    res = []
    i = 1
    while i * i <= num:
        if num % i == 0:
            res.append(i)
            if i != (num // i): # avoid duplicate
                res.append(num // i)
        i += 1
    return res

print(factors(48))
print(factors(36))

'''
Ram and Shyam are sitting next to each other, hoping to cheat on an exam. However, the examination board has prepared 
p different sets of questions (numbered 0 through p−1), which will be distributed to the students in the following way:

The students are assigned roll numbers — pairwise distinct positive integers.
If a student's roll number is r, this student gets the ((r−1)%p)-th set of questions.
Obviously, Ram and Shyam can cheat only if they get the same set of questions.

You are given the roll numbers of Ram and Shyam: 
A and B respectively. Find the number of values of p for which they can cheat, or determine that there is an infinite number of such values.
'''