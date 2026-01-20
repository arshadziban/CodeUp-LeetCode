def caesar_cipher(text, shift):
    result = ""
    emojis = ["😀", "😂", "😍", "🤔", "😎", "🎉", "🚀", "💡", "🌟", "❤"]

    for char in text:
        if char.isalpha():
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')

            new_position = (ord(char) - start + shift) % 26
            new_char = chr(new_position + start)

            result += new_char
            
        elif char.isdigit():
            new_position = (int(char) + shift) % 10
            new_char = str(new_position)
            result += new_char
            
        elif char in emojis:
            current_index = emojis.index(char)
            new_index = (current_index + shift) % len(emojis)
            result += emojis[new_index]
        else:
            result += char

    return result
 


def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)


message = "Hello, Zorld! 129 ❤"
shift_value = 5

encrypted = caesar_cipher(message, shift_value)
decrypted = caesar_decipher(encrypted, shift_value)

print("Original:", message)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
