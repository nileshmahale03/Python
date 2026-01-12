def generate_all_subsequences(arr):
    """
    Prints all subsequences of the given array (non-contiguous allowed).
    Total subsequences = 2^N
    """
    n = len(arr)

    def backtrack(idx, path):
        if idx == n:
            print(path)
            return

        # Not take
        backtrack(idx + 1, path)

        # Take
        path.append(arr[idx])
        backtrack(idx + 1, path)
        path.pop()

    backtrack(0, [])

def get_all_subsequences(arr):
    """
    Returns a list of all subsequences.
    """
    n = len(arr)
    result = []

    def backtrack(idx, path):
        if idx == n:
            result.append(path.copy())
            return

        backtrack(idx + 1, path)
        path.append(arr[idx])
        backtrack(idx + 1, path)
        path.pop()

    backtrack(0, [])
    return result


# usage
A = [1, 6, 3, 7]
generate_all_subsequences(A)

all_subsequences = get_all_subsequences(A)

for sub in all_subsequences:
    print(sub)