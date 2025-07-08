def length_of_longest_substring(s):
    char_index = {}
    start = max_len = 0

    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = i
        max_len = max(max_len, i - start + 1)

    return max_len

print(length_of_longest_substring("abcabcbb"))   
print(length_of_longest_substring("bbbbb"))      

