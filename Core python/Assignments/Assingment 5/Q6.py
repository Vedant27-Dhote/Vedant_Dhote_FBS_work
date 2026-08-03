'''Write a program to print first n prime numbers.'''

n = int(input("Enter how many prime numbers you want to print: "))

count = 0      
num = 2        
print(f"\nThe first {n} prime numbers are:")

while count < n:
    is_prime = True
    
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break  
            
    if is_prime:
        print(num, end=" ")
        count += 1
        
    num += 1

