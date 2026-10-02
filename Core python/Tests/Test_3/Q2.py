'''Write a program to calculate the sum of following series
where n is input by user.
1/1! + 2/2! + 3/3! + 4/4! + ... N/N!'''

n = int(input("Enter the value of n: "))
sum_series = 0
for i in range(1, n + 1):
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    sum_series += i / factorial

print(f"The sum of the series up to {n} is: {sum_series}")
