def first_non_repeated_char(s: str):
    char_count = {}
    
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in s:
        if char_count[char] == 1:
            return char
    return None


# Test cases
print(first_non_repeated_char("swiss")) 
