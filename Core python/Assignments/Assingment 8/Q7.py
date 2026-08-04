'''Write a program to find sum of digits of a number.'''
def sum_of_digits(number):
    number = abs(number)
    total_sum = 0
    
    while number > 0:
        digit = number % 10
        total_sum += digit
        number = number // 10
        
    return total_sum

num = 12345
result = sum_of_digits(num)
print(f"The sum of digits of {num} is: {result}")

