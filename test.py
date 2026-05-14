key = "CRYPTO"
cipher = "CQOBZKVGSKBVACAICAGEQBZAPGHC"

# Create Matrix
s = ""

for ch in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
    if ch not in s:
        s += ch

matrix = [s[i:i+5] for i in range(0, 25, 5)]

print("Matrix:\n")

for row in matrix:
    print(row)


# Find Position
def find(ch):

    for i in range(5):
        for j in range(5):

            if matrix[i][j] == ch:
                return i, j


# Playfair Decryption
plain = ""

for i in range(0, len(cipher), 2):

    a, b = cipher[i], cipher[i+1]

    r1, c1 = find(a)
    r2, c2 = find(b)

    if r1 == r2:

        plain += matrix[r1][(c1-1)%5]
        plain += matrix[r2][(c2-1)%5]

    elif c1 == c2:

        plain += matrix[(r1-1)%5][c1]
        plain += matrix[(r2-1)%5][c2]

    else:

        plain += matrix[r1][c2]
        plain += matrix[r2][c1]

print("\nDecrypted Text:")
print(plain)

# Readable Plaintext
text = "PLEASE MAKE A WORD GROUP AND VERIFY"

# Count Words
shift = len(text.split())

print("\nTotal Words:", shift)


# Caesar Encryption
result = ""

for ch in text:

    if ch.isalpha():

        x = (ord(ch.upper()) - 65 + shift) % 26
        result += chr(x + 65)

    else:
        result += ch

print("\nCaesar Encrypted Text:")
print(result)