
def is_power_of_two(n: int) -> bool:
    """
    Returns True if n is a power of 2, otherwise False.
    """
    return n > 0 and (n & (n - 1)) == 0

# usage
print(is_power_of_two(8))
print(is_power_of_two(9))