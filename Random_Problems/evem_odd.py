def classify_number(n):
    """Classify a number by multiple properties"""
    properties = {}
    
    # Even/Odd classification
    properties['parity'] = 'even' if n % 2 == 0 else 'odd'
    
    # Prime check
    properties['prime'] = is_prime(n)
    
    # Perfect square check
    properties['perfect_square'] = int(n ** 0.5) ** 2 == n
    
    # Digit sum
    properties['digit_sum'] = sum(int(digit) for digit in str(abs(n)))
    
    # Factors
    properties['factors'] = get_factors(n)
    
    return properties

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def get_factors(n):
    """Get all factors of a number"""
    n = abs(n)
    if n == 0:
        return []
    return [i for i in range(1, n + 1) if n % i == 0]

# Main program
try:
    a = int(input("Enter value of a: "))
    result = classify_number(a)
    
    print(f"\n--- Number Analysis for {a} ---")
    print(f"Parity: {result['parity'].capitalize()}")
    print(f"Prime: {'Yes' if result['prime'] else 'No'}")
    print(f"Perfect Square: {'Yes' if result['perfect_square'] else 'No'}")
    print(f"Digit Sum: {result['digit_sum']}")
    print(f"Factors: {result['factors']}")
    
except ValueError:
    print("Error: Please enter a valid integer")
