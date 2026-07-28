# WAP to print all numbers in a range divisible by a given number.
a = int(input("Enter the starting of range(Greater than 0) :"))
b = int(input("Enter the ending of range :"))

n = int(input("Enter the number to divide"))

for i in range(a,b):
    if i % n==0:
        print(i, end=" ")