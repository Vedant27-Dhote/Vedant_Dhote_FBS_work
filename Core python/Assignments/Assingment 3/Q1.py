#Write a program to check if the given number is positive or negative.

num = int(input("Enter the number:-"))

if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("invalid input or you have entered 0 which is neutral")