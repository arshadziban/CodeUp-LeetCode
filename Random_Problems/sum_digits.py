# Take input from user
num = input("Enter a number: ")

# Initialize sum variable
sum_digits = 0

# Loop through each digit in the number
for digit in num:
    sum_digits += int(digit)

# Print the sum of digits
print("Sum of the digits:", sum_digits)
