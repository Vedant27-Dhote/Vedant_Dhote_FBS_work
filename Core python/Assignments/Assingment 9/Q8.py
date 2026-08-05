def is_prime(n, divisor=2):
    if n <= 2:
        return True if n == 2 else False
    if n % divisor == 0:
        return False
    if divisor * divisor > n:
        return True
    return is_prime(n, divisor + 1)


num = 17
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is NOT a prime number.")
