def vowel():
    char = input("Enter a character: ").strip().lower()
    if len(char) != 1 or not char.isalpha():
        print("Please enter a single alphabetic character.")
        return
    if char in 'aeiou':
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is not a vowel.")

vowel()