"""
Python Operator Precedence & Associativity
-----------------------------------------

Precedence: Order in which operators are evaluated
Associativity: Direction of evaluation when precedence is same
"""

# Highest to Lowest Precedence

# 1. Parentheses
# ()

# 2. Exponentiation (Right to Left)
# **

# 3. Unary operators
# +x, -x, ~x

# 4. Multiplicative
# *, /, //, %

# 5. Additive
# +, -

# 6. Bitwise shifts
# <<, >>

# 7. Bitwise AND
# &

# 8. Bitwise XOR
# ^

# 9. Bitwise OR
# |

# 10. Comparison
# < <= > >= == !=

# 11. Logical NOT
# not

# 12. Logical AND
# and

# 13. Logical OR
# or

# 14. Assignment (Right to Left)
# = += -= *= /= %= **=

# Examples
print(2 + 3 * 4)      # 14
print(2 ** 3 ** 2)    # 512
print(-3 ** 2)        # -9
print((N := 8) > 0 and (N & (N - 1)) == 0)

