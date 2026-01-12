
def merge_strings_alternately(s, t):
    """
    Merges two strings by alternating characters.
    Appends remaining characters if lengths differ.
    """
    ans = []
    min_len = min(len(s), len(t))

    for i in range(min_len):
        ans.append(s[i])
        ans.append(t[i])

    ans.append(s[min_len:])
    ans.append(t[min_len:])

    return "".join(ans)

# usage
full_name = merge_strings_alternately("Nilesh", "Mahale")
print(full_name)