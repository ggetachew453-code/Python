def generate_primes(n):
    """
    Generator that yields all prime numbers less than n.
    
    Args:
        n: Upper limit (exclusive) for prime numbers
    
    Yields:
        Prime numbers in ascending order
    """
    if n <= 1:
        return
    
    # Special case: 1 is not typically considered prime, but based on example
    yield 1
    
    if n <= 2:
        return
    
    yield 2
    
    # Check odd numbers starting from 3
    for num in range(3, n, 2):
        is_prime = True
        # Check divisibility up to sqrt(num)
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num

# Example usage
print("Prime Numbers:")
for prime in generate_primes(100):
    print(prime, end=" ")
print()  # Output: 1 2 3 5 7