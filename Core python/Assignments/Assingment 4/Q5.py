# WAP to print Fibonacci series upto n.
n = int(input("Enter the number upto which you want fibonacci series:"))
a = 0
b = 1
for i in range(1,n+1):
    print(a,end=" ")
    
    a,b= b, a+b
    

