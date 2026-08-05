def sum_n(n):
    if n <= 1:
        return n
    return n + sum_n(n - 1)


num = 5  
print("Sum of first n numbers:", sum_n(num))
