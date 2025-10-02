def fizzbuzz_variant(start, end):
    if start > end:
        return  # Print nothing if start > end
    
    for num in range(start, end + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 2 == 0:
            print(f"{num} Even")
        else:
            print(num)