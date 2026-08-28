class Mobile:
    def __init__(self,company,colour,battery):
        self.company = company
        self.colour = colour
        self.battery = battery

    def getCompany(self):
        return self.company
    def setCompany(self,newCompany):
        self.company = newCompany

    def getColour(self):
        return self.colour
    def setColour(self,newColour):
        self.colour= newColour

    def getBattery(self):
        return self.battery
    def setBattery(self,newBattery):
        self.battery = newBattery

car = Mobile("Pixel","Black","6000mah")

print(car.getColour())


        