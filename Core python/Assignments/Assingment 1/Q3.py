#Program to find quotient and remainder of two numbers.
dividend = float(input("Enter the dividend:-"))
divisor = float(input("Enter the divisor:-"))

quotient = dividend // divisor
remainder = dividend % divisor

print(f"Quotient: {quotient}")
print(f"Remainder: {remainder}")