'''WAP to check if a given number is Armstrong number or not. For
each task create separate functions.'''
def count_digits(number):
    return len(str(number))

def calculate_armstrong_sum(number, power):
    total_sum = 0
    temp = number
    
    while temp > 0:
        digit = temp % 10
        total_sum += digit ** power
        temp = temp // 10
        
    return total_sum

def is_armstrong(number):
    power = count_digits(number)
    armstrong_sum = calculate_armstrong_sum(number, power)
    return armstrong_sum == number

num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
