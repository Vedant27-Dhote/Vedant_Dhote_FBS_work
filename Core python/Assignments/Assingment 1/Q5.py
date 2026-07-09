#Write a program to enter P, T, R and calculate Compound Interest.
p = float(input("Enter Principal amount (P): "))
t = float(input("Enter Time period in years (T): "))
r = float(input("Enter Rate of interest (R): "))

# Calculate total amount
amount = p * ((1 + r / 100) ** t)

# Calculate compound interest
compound_interest = amount - p

print(f"Total Amount: {amount}")
print(f"Compound Interest: {compound_interest}")

