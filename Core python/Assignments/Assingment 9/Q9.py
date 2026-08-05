def power(m, n):
    if n == 0:
        return 1
    return m * power(m, n - 1)

base = 2
exponent = 5  
print(f"{base} to the power {exponent} is:", power(base, exponent))
