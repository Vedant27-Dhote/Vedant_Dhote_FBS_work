'''Write a program to check if entered number is a palindrome or
not.'''
def is_palindrome(number):
    original_num = number
    reversed_num = 0
    
    while number > 0:
        digit = number % 10
        reversed_num = (reversed_num * 10) + digit
        number = number // 10
        
    return original_num == reversed_num

num = 12321
print(is_palindrome(num))  
