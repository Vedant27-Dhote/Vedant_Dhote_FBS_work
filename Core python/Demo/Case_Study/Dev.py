from Emp import Emp

class Dev(Emp):
    def __init__(self, id, name, sal, bonus):
        super().__init__(id, name, sal)
        self.bonus = bonus

    def getBonus(self):
        return self.bonus

    def setBonus(self, newBonus):
        self.bonus = newBonus

    def calSal(self):
        return self.sal + self.bonus

    def __str__(self):
        return f"Developer -> ID: {self.id}, Name: {self.name}, Base: {self.sal}, Bonus: {self.bonus}, Total: {self.calSal()}"
