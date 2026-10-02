'''Write a program to print first n prime numbers'''

first_n = int(input("Enter the value of n: "))
count = 0
num = 2
while count < first_n:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num)
        count += 1
    num += 1
