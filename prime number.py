def generate_primes(n):
    
    

    if n <= 1:
        return
    
    
    yield 1
    
    if n <= 2:
        return
    
    yield 2
    

    for num in range(3, n, 2):
        is_prime = True
        # Check divisibility up to sqrt(num)
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num


print("Prime Numbers:")
for prime in generate_primes(100):
    print(prime, end=" ")
print()  
