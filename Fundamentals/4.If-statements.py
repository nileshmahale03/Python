#if statements
def is_balance_low(balance: int) -> None:
    if balance <= 100:
        print("Warning: Low balance.")

is_balance_low(99)
is_balance_low(100)
is_balance_low(101)

#if-else statements
def get_min(a: int, b: int) -> int:
    if a < b:
        return a
    else:
        return b

print(get_min(10, 11))
print(get_min(5, -7))
print(get_min(20, 20))

#if elif else statements
def check_range(num: int) -> str:
    if num < 0:
        return "negative"
    elif num == 0:
        return "zero"
    elif num < 10:
        return "positive single digit"
    else:
        return "positive multi digit"

print(check_range(-10))
print(check_range(0))
print(check_range(9))
print(check_range(1000))

#Logic Condition
def discount_applies(age: int) -> bool:
    if age < 18 or age >=65:
        return True
    return False

print(discount_applies(17))
print(discount_applies(18))
print(discount_applies(40))
print(discount_applies(65))
print(discount_applies(70))

'''
A value is falsy if it is:

False (boolean)
None  (NoneType)
0     (integer)
0.0   (float)
""    (empty string)
[]    (empty list)
Most other empty collections (e.g. empty tuple, empty set, empty dictionary)

A value is truthy if it is:

True (boolean)
All integers other than 0
All floats other than 0.0
All strings other than ""
All collections with at least one element
'''
