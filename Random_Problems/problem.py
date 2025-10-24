# sum numbners and divide by 2 then if this number is even print even else print odd
def process_numbers():
    user_input1 = input("Enter first number: ")
    user_input2 = input("Enter second number: ")
    
    total = float(user_input1) + float(user_input2)
    average = total / 2
    
    if average % 2 == 0:
        print("The average is even:", average)
    else:
        print("The average is odd:", average)
process_numbers()