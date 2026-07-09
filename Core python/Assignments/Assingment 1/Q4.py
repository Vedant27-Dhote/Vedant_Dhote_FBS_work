#Write a program to enter P, T, R and calculate simple Interest.
P = float(input("Enter the principal amount:-"))
T = float(input("Enter the time period in months:-"))
R = float(input("Enter the rate of intrest:-"))

Simple_intrest = (P*T*R)/100 # Formula for simple intrest

print(f"The Simple intrest for your Amount is:-{Simple_intrest}")