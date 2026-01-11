
'''
“input() is a built-in Python function that reads user input as a string.
To work with numbers, we explicitly convert it using int(), float(), or map() for multiple inputs.”
'''
s = input()
age = int(input())

a, b = map(int, input().split())

arr = list(map(int, input().split()))

'''
	•	strip() is a string method
	•	It removes leading and trailing whitespace
	•	It does NOT remove spaces in the middle
'''
s = "   hello   "
print(s.strip())   # "hello"


'''
	•	.2f → fixed-point with 2 decimal places
	•	.6g → general format with 6 significant digits
'''
x = 3.14159

print(f"{x:.2f}")   # 3.14
print(f"{x:.6g}")   # 3.14159