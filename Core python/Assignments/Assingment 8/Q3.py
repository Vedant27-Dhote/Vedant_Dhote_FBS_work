
def calculate_factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

def sum_series_a(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def sum_series_b(n):
    total = 0
    for i in range(1, n + 1):
        total += calculate_factorial(i)
    return total


def sum_series_c(n):
    
    total = 0
    for i in range(1, n + 1):
        total += i ** i
    return total

n = int(input("Enter the value of n: "))

print("Results for n =", n)
print("a. Sum of natural numbers =", sum_series_a(n))
print("b. Sum of factorials =", sum_series_b(n))
print("c. Sum of powers =", sum_series_c(n))
