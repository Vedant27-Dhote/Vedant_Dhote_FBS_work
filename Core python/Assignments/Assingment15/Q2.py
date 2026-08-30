'''Create a class Product with members as pid,pname,price and quantity .Add
following methods:
d. Constructor (Support both parameterized and parameterless)
e. Destructor
f. ShowBook'''


class Product:
    def __init__(self,pid,pname,price,quantitiy):
        self.pid=pid
        self.pname=pname
        self.price=price
        self.quantity=quantitiy

    def getPid(self):
        return self.pidid
    def setPid(self,newPid):
        self.pid=newPid

    def getPname(self):
        return self.pname
    def setPname(self,newPname):
        self.pname=newPname

    def getprice(self):
        return self.price
    def setPrice(self,newPrice):
        self.price=newPrice

    def getQuantity(self):
        return self.quantity
    def setQuantity(self,newQuantity):
        self.quantity=newQuantity



    def __del__(self):
        pass

    def showproduct(self):
        print(f"product_id={self.pid}, Product_name={self.pname}, Price={self.price}, Quantity={self.quantity}")

b1 = Product(121,"Mobile",4500,2)
b1.showproduct()
    