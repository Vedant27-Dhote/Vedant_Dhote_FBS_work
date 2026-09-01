'''Create a class Book with members as bid,bname,price and author.Add following
methods:
a. Constructor (Support both parameterized and parameterless)
b. Destructor
c. ShowBook
d. Add static variable count and also maintain count of objects created.'''

class Book:
    count=0
    def __init__(self,bid=0,bname="none",price=0,author="none"):
        self.bid=bid
        self.bname=bname
        self.price=price
        self.author=author
        Book.count+=1

    def getBid(self):
        return self.bid
    def setBid(self,newBid):
        self.bid=newBid

    def getBname(self):
        return self.bname
    def setBname(self,newBname):
        self.bname=newBname

    def getprice(self):
        return self.price
    def setPrice(self,newPrice):
        self.price=newPrice

    def getAuthor(self):
        return self.author
    def setAuthor(self,newAuthor):
        self.author=newAuthor



    def __del__(self):
        pass

    def showbook(self):
        print(f"Book_id={self.bid}, Book_name={self.bname}, Price={self.price}, author={self.author}")

b1 = Book(121,"Silent Paitent",4500,"van der rossum")
b2 = Book(1,"Ikigai",1000,"mine")
b1.showbook()
print(Book.count)