
def generate_all_subarrays(arr):
    """
    Generates and returns all contiguous subarrays of the given array.
    """
    n = len(arr)
    subarrays = []

    for i in range(n):
        for j in range(i, n):
            subarrays.append(arr[i:j + 1])

    return subarrays


# usage
A = [1, 6, 3, 7]
all_subarrays = generate_all_subarrays(A)

for sub in all_subarrays:
    print(sub)