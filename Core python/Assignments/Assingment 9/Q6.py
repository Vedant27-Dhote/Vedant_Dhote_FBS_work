def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

terms = 7
print(f"Fibonacci series up to {terms} terms:")
for i in range(terms):
    print(fibonacci(i), end=" ")
print()
