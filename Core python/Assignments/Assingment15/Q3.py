'''Create a class Shirt with members as sid,sname,type(formal etc), price and
size(small,large etc) .Add following methods:
g. Constructor (Support both parameterized and parameterless)
h. Destructor
i. ShowShirt'''

class Shirt:
    def __init__(self,sid,sname,type,price,size):
        self.sid=sid
        self.sname=sname
        self.type=type
        self.price=price
        self.size=size

    def getSid(self):
        return self.sid
    def setSid(self,newSid):
        self.sid=newSid

    def getSname(self):
        return self.sname
    def setSname(self,newSname):
        self.sname=newSname

    def getType(self):
        return self.type
    def setType(self,newType):
        self.type=newType

    def getprice(self):
        return self.price
    def setPrice(self,newPrice):
        self.price=newPrice

    def getSize(self):
        return self.size
    def setSize(self,newSize):
        self.size=newSize

    def showShirt(self):
        print(f"Shirt_id={self.sid}, Shirt_name={self.sname},Shirt_type={self.type}, Price={self.price}, Size={self.size}")


s1 = Shirt(1,"cheque","Formal",2000,"M")
s1.showShirt()