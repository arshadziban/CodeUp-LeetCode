def vowel():
    char = input("Enter a character: ").lower()
    if char in 'aeiou':
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is not a vowel.")
        
vowel()