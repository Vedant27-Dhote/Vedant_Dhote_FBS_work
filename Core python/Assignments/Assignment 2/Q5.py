# Q. WAP to calculate selling price of book based on cost price and discount.
cost = float(input("Enter the cost price of Book:-"))
Discount = float(input("Enter discout in percentage (e.g:- 5percent etc):-"))

Selling = cost - ((cost*Discount)/100)

print(f"The selling price of a Book is { Selling}Rs")