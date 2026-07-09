#Q. Write a program to swap two numbers without using third variable.
a = int(input("Enter the number1:-"))
b = int(input("Enter the number2:-"))

a = a + b
b = a - b
a = a - b

print(f"1st number becomes {a} and 2nd number becomes {b}")