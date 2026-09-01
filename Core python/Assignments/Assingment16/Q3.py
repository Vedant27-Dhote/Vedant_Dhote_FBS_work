'''Create a class Shirt with members as sid,sname,type(formal etc), price and
size(small,large etc) .Add following methods:
j. Constructor (Support both parameterized and parameterless)
k. Destructor
l. ShowBook
m. For each size of shirt price should change by 10%.
(eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
xlarge=1300) Use static concept.'''

class Shirt:
    @staticmethod
    def get_factor(size):
        size = size.lower()
        if size == "small":
            return 1.0
        elif size == "medium":
            return 1.1 
        elif size == "large":
            return 1.2  
        elif size == "xlarge":
            return 1.3  
        else:
            return 1.0

    def __init__(self, sid=0, sname="Unknown", type="Formal", price=0.0, size="Small"):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.size = size
        
        self.price = price * Shirt.get_factor(size)


    def ShowBook(self):
        print(f"ID: {self.sid}  Name: {self.sname}  Type: {self.type}  Size: {self.size}  Price: {self.price}")


shirt1 = Shirt()
shirt1.ShowBook()

shirt2 = Shirt(101, "Louis Philippe", "Formal", 1000, "Small")
shirt3 = Shirt(102, "Louis Philippe", "Formal", 1000, "Medium")
shirt4 = Shirt(103, "Louis Philippe", "Formal", 1000, "Large")
shirt5 = Shirt(104, "Louis Philippe", "Formal", 1000, "XLarge")

shirt2.ShowBook()
shirt3.ShowBook()
shirt4.ShowBook()
shirt5.ShowBook()
