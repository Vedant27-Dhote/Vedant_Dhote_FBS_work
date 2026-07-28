# WAP to print all odd numbers until n.
n = int(input("Enter the number till you want odd numbers:"))

print("The odd numbers are:")

for i in range(1,n+1):
    if i%2!=0:
        print(i,end=" ")
