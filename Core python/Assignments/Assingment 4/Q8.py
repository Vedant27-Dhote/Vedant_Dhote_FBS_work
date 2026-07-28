# WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.
a = int(input("Enter starting of range:"))
b = int(input("Enter ending og range:"))

for i in range(a,b):
    if i%7==0 and i%5==0:
        print(i,end=" ")