from abc import ABC,abstractmethod
class Emp(ABC):
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
    @abstractmethod
    def calSal(self):
        pass

    

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

class Dev(Emp):
    def __init__(self, id, name, sal,bonus):
        super().__init__(id, name, sal)
        self.bonus = bonus

    def getBonus(self):
        return self.bouns
    def setBonus(self,Newbonus):
        self.bouns= Newbonus

    def calSal(self):
        return self.bonus+self.sal


#e1 = Emp(103,"Dhoni",98000)
d1 = Dev(101,"Vedant",75000,8000)
h1 = Hr(102,"Viart",68000,5000)
print(d1)

