#Counter
from collections import Counter
A = [1, 2, 3, 4, 5, 3, 2, 1, 5, 3]

freq = Counter(A)

# usage
print(dict(freq))

def build_frequency_dict(s):
    """
    Returns a dictionary with character frequencies of the string.
    """
    freq = {}

    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    return freq

# usage
word = "hello"
print(build_frequency_dict(word))