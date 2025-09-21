def div():
    num = int(input("Enter numerator: "))
    
    if num == 0:
        print("Numerator cannot be zero.")
    if num % 5 == 0 and num % 11 == 0:
        print(f"{num} is divisible by both 5 and 11.")
    elif num % 5 == 0:
        print(f"{num} is divisible by 5.")
    elif num % 11 == 0:
        print(f"{num} is divisible by 11.")

div()