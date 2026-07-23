#Write a program to calculate profit or loss.
price = int(input("Enter the price:"))
selling = int(input("Enter the selling price of book:"))

amount = selling - price

if amount>0:
    print(f"Profit of {amount}rs")
else:
    print(f"Loss of {amount}rs")