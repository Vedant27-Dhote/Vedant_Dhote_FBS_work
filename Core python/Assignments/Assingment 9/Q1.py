def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def sum_of_series(n):
    if n <= 1:
        return 1
    return factorial(n) + sum_of_series(n - 1)


num = int(input("Enter n: "))
print(f"Sum of the series: {sum_of_series(num)}")
