# Take input from user
num = int(input("Enter a number: "))

# Initialize factorial
factorial = 1

# Loop to calculate factorial
for i in range(1, num + 1):
    factorial *= i

# Print result
print(num, "factorial is:", factorial)
