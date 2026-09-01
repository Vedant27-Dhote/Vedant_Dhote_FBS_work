'''Create a class Product with members as pid,pname,price and quantity .Add
following methods:
e. Constructor (Support both parameterized and parameterless)
f. Destructor
g. ShowBook
h. Add static method discount.
i. Provide methods for applying discount on price of product.'''
class Product:
    discount = 0
    def __init__(self, pid=0, pname="None", price=0.0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity


    
    def ShowBook(self):
        print(f"ID: {self.pid} | Name: {self.pname} | Price: ${self.price} | Qty: {self.quantity}")

    def apply_discount(self):
        self.price = self.price - (self.price * Product.discount / 100)


p1 = Product()
p1.ShowBook()


p2 = Product(101, "Comic Book", 50.0, 5)
p2.ShowBook()

Product.discount = 10

p2.apply_discount()
p2.ShowBook()
