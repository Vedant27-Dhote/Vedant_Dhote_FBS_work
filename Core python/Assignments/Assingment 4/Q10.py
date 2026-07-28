# WAP to check if given number is Perfect Number.
n = int(input("Enter the number :"))
count = 0

for i in range(1,n):
    if n%i==0:
        count+=i


if count == n:
    print("The number is Perfect number")
else:
    print("The is not Perfect")