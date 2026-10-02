'''Write a program to accept 3 digit number. If first digit is double of second digit and half of
third digit then display “Yes, you have done it”, otherwise display “Please try next time”.
Eg : - 428 , 214 etc.'''
number = int(input("Enter a 3-digit number: "))

first_digit = number // 100
second_digit = (number // 10) % 10
third_digit = number % 10

if first_digit == 2 * second_digit and first_digit == third_digit / 2:
    print("Yes, you have done it")
else:
    print("Please try next time")