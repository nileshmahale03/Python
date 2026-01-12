
def count_non_decreasing_subarrays(arr):
    """
    Returns the number of non-decreasing contiguous subarrays.
    """
    n = len(arr)
    if n == 0:
        return 0

    ans = 0
    streak = 1

    for i in range(1, n):
        if arr[i] >= arr[i - 1]:
            streak += 1
        else:
            ans += streak * (streak + 1) // 2
            streak = 1

    # add last streak
    ans += streak * (streak + 1) // 2
    return ans


# usage
print(count_non_decreasing_subarrays([1, 6, 3, 7]))
print(count_non_decreasing_subarrays([1, 6, 9, 3, 7]))