def build_frequency_array(arr):
    """
    Builds and returns a frequency array for values from 1 to len(arr).
    """
    freq = [0] * (len(arr) + 1)

    for value in arr:
        freq[value] += 1

    return freq

# usage
A = [1, 2, 3, 4, 5, 3, 2, 1, 5, 3]
freq = build_frequency_array(A)

for i in range(1, len(freq)):
    print(freq[i], end=" ")