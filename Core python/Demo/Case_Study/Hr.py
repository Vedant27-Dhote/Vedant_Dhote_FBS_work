from Emp import Emp

class Hr(Emp):
    def __init__(self, id, name, sal, comission):
        super().__init__(id, name, sal)
        self.comission = comission

    def getComission(self):
        return self.comission

    def setComission(self, newComission):
        self.comission = newComission

    def calSal(self):
        return self.comission + self.sal

    def __str__(self):
        return f"HR -> ID: {self.id}, Name: {self.name}, Base: {self.sal}, Commission: {self.comission}, Total: {self.calSal()}"
