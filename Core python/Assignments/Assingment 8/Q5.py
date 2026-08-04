'''sum of all prime number between 1 to n'''
def sum_of_primes(n):
    total_sum = 0
    for num in range(2, n + 1):
        is_prime = True
        
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break  
                
        
        if is_prime:
            total_sum += num
            
    return total_sum

n = 10
result = sum_of_primes(n)
print(f"The sum of all prime numbers between 1 and {n} is: {result}")

