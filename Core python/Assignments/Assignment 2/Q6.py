#Q. WAP to calculate total salary of employee based on basic, da=10% of basic,ta=12% of basic, hra=15% of basic.

Basic = float(input("Enter the Basic salary:-"))

Total = (Basic*10)/100 + (Basic*12)/100 + (Basic*15)/100

print(f"The Total salary is{Total}")