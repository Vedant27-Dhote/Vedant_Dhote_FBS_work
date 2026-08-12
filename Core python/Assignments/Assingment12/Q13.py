'''Python Program to count number of digits and letters in a string.'''

def count_letters_and_digits(text):
    letters = 0
    digits = 0
    
    for char in text:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
            
    print(f"Letters: {letters}")
    print(f"Digits: {digits}")


user_input = input("Enter a string: ")
count_letters_and_digits(user_input)
