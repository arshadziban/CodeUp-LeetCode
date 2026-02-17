key = "MONARCHY"
text = "BALLON"


# create matrix
def create_matrix(key):
    key = key.upper().replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" 
    result = ""

    # add key letters first
    for letter in key:
        if letter not in result:
            result += letter

    # add remaining letters
    for letter in alphabet:
        if letter not in result:
            result += letter

    # make 5x5 matrix
    matrix = []
    for i in range(0, 25, 5):
        matrix.append(list(result[i:i+5]))

    return matrix


# Prepare text
def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = text.replace(" ", "")
    new_text = ""
    i = 0

    while i < len(text):
        if i + 1 < len(text):
            if text[i] == text[i+1]:
                new_text += text[i] + "X"
                i += 1
            else:
                new_text += text[i] + text[i+1]
                i += 2
        else:
            new_text += text[i] + "X"
            i += 1

    return new_text




matrix = create_matrix(key)

print("Key Matrix:")
for row in matrix:
    print(row)
