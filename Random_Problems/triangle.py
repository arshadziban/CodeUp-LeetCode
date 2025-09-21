a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))



if a + b > c and a + c > b and b + c > a:
    print("These sides can form a triangle")
else:
    print("These sides cannot form a triangle")
