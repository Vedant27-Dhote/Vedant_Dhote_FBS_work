class Emp:
    def __init__(self,id,name,sal):
        self.id=id
        self.name = name
        self.sal = sal

    def getid(self):
        return self.id
    def setid(self,Newid):
        self.id=Newid
    def getName(self):
        return self.name
    def setName(self,newName):
        self.name = newName
    def getSal(self):
        return self.sal
    def setSal(self,newSal):
        self.sal=newSal

    def calSal(self):
        return self.sal

    def __str__(self):
        return f"Id={self.id}\tName={self.name}\tSalary={self.sal}"

    

class Hr(Emp):
    def __init__(self, id, name, sal,comission):
        super().__init__(id, name, sal)
        self.comission=comission

    def getComission(self):
            return self.comission
    def setComission(self,Newcomission):
            self.comission= Newcomission

    def calSal(self):
        return self.comission+self.sal

    def __str__(self):
        return super().__str__()+f"\tComission={self.comission}"

class Dev(Emp):
    def __init__(self, id, name, sal,bonus):
        super().__init__(id, name, sal)
        self.bonus = bonus

    def getBonus(self):
        return self.bouns
    def setBonus(self,Newbonus):
        self.bonus= Newbonus

    def calSal(self):
        return self.bonus+self.sal

    def __str__(self):
        return super().__str__()+f"\tBonus={self.bonus}"



s1 = Dev(101,"Vedant",75000,8000)
print(s1.calSal())
print(s1)