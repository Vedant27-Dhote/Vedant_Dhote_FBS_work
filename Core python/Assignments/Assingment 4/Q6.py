# WAP to check if a given number is prime number or not.
n = int(input("Enter the number:"))

if n>1:
    for i in range(2,n):
        if n%i==0:
            print("The number is not prime")
            break
    else:
        print("The number is prime")
        
else:
    print("The number is not prime")