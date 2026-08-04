'''Write a program find reverse of a number'''
def reverse_number(number):
    
    reversed_num = 0
    
    while number > 0:
        digit = number % 10
        
        reversed_num = (reversed_num * 10) + digit
        
        number = number // 10
        
    return  reversed_num


num = 12345
result = reverse_number(num)
print(f"The reverse of {num} is: {result}")

