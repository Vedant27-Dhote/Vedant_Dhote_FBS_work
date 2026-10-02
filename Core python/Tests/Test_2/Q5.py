'''A man goes for shopping. He buys 5 products. Accept the price of all products and display
the total bill after adding 18% GST'''
product1 = float(input("Enter the price of product 1: "))
product2 = float(input("Enter the price of product 2: "))
product3 = float(input("Enter the price of product 3: "))
product4 = float(input("Enter the price of product 4: "))
product5 = float(input("Enter the price of product 5: "))

total_price = product1 + product2 + product3 + product4 + product5
gst = total_price * 0.18
total_bill = total_price + gst
print(f"Total bill after adding 18% GST: Rs. {total_bill}")