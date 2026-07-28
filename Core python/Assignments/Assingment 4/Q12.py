# Write a program to check if given number is Armstrong number or not.
number = int(input("Enter a number to check: "))
num_digits = len(str(number))

temp = number
armstrong_sum = 0

while temp > 0:
    digit = temp % 10
    armstrong_sum += digit ** num_digits
    
    temp //= 10

if armstrong_sum == number:
    print(f"{number} is an Armstrong Number!")
else:
    print(f"{number} is NOT an Armstrong Number.")
