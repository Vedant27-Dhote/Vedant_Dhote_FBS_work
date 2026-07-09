#Q. Write a program to reverse three-digit number. tell me logic
num = int(input("Enter a 3-digit number: "))


last_digit = num % 10
middle_digit = (num // 10) % 10
first_digit = num // 100


reversed_num = (last_digit * 100) + (middle_digit * 10) + first_digit

print(f"Reversed number: {reversed_num}")