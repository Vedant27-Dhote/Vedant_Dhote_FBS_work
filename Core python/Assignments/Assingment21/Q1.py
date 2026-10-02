'''Develop a simple calculator program that performs basic arithmetic operations (+,
-, *, /) on two numbers provided by the user. The program should ask the user for
the numbers and the operator. However, the program should handle the following
exceptions:
a. Invalid Number: If the user enters a number that is not valid, catch the
exception and display an error message.
b. Invalid Operator: If the user enters an operator other than "+", "-", "*", or
"/", catch the exception and display an error message.
c. Division by Zero: If the user tries to divide by zero, catch the exception and
display an error message.
Write a program that performs the requested arithmetic operation and
handles the exceptions as described above.'''

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    
    op = input("Enter operator: ")

    if op not in ["+", "-", "*", "/"]:
        raise Exception("Invalid Operator")

    if op == "+":
        print("Result =", a + b)

    elif op == "-":
        print("Result =", a - b)

    elif op == "*":
        print("Result =", a * b)

    elif op == "/":
        print("Result =", a / b)

except ValueError:
    print("Invalid Number")

except ZeroDivisionError:
    print("Cannot divide by zero")

except Exception as e:
    print(e)