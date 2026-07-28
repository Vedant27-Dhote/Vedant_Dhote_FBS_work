#WAP to print factorial of a number .

a = int(input("Enter the number to print factorial:"))
b = 1

for i in range(1,a+1):
    b*=i

print(f"The factorial of {i} is {b}")
