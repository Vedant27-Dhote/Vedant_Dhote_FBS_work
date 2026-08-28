class Vehicle:
    def __init__(self,chasis,colour,brand):
        self.chasis = chasis
        self.colour = colour
        self.brand = brand

    def getChasis(self):
        return self.chasis
    def setChasis(self,newChasis):
        self.chasis = newChasis

    def getColour(self):
        return self.colour
    def setColour(self,newColour):
        self.colour= newColour

    def getBrand(self):
        return self.brand
    def setBrand(self,newBrand):
        self.brand = newBrand

car = Vehicle(1234,"Black","Skoda")

print(car.getColour())


        