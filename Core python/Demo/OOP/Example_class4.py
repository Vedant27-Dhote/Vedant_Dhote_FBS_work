# We are doing inhertitance
class Electronic_device:
    count = 0
    def __init__(self,type,colour,brand):
        self.type=type
        self.colour=colour
        self.brand=brand
        Electronic_device.count+=1

    def display(self):
        print(f"Type of device={self.type}  colour of device={self.colour}  brand of device={self.brand}")


class Mobile(Electronic_device):
    def __init__(self, type, colour, brand,battery):
        super().__init__(type, colour, brand)
        self.battery=battery

    def display(self):
        super().display()
        print(f"Battery capacity={self.battery}")


s1=Mobile("Android","Black","Google","6000mah")
s1.display()

        