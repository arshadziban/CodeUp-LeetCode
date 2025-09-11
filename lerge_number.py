def large_number():
   q = int(input("Enter a number: "))
   b = int(input("Enter another number: "))
   c= int(input("Enter one more number: "))
   
   max_num = max(q, b, c)
   print("The largest number is:", max_num)
   
large_number()