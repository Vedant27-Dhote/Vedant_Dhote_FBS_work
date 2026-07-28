# WAP to print sum of series upto n.
n = int(input("Enter the number : "))

count = 0

for i in range (1,n+1): 
    count += i
print(f"Sum of series is : {count}")