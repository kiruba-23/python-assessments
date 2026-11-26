class vehicle:
    def __init__(self):
        self.Brandname=input("Enter your brandname: ")
        self.Modelname=input("Enter your model name:")
    def display(self):
        print("My Brand name:",self.Brandname)
        print("My Model name:",self.Modelname)
    def cardetai(self):
        print("MY CAR DETAILS")
        print("_________________")
    def bikedetai(self):
        print("MY BIKE DETAILS")
        print("_________________")

class car(vehicle):
    def __init__(self):
        super().__init__()
        self.fueltype=input("Enter your fuel type: ")
        self.seats=input("enter your seating capacity: ")
    def dispalycar(self):
        print("My car fuel type",self.fueltype)
        print("My car seating capacity:",self.seats)

class bike(vehicle):
    def __init__(self):
        super().__init__()
        self.Engine=input("Enter your Engine type: ")
        self.Milage=input("Enter your Milage: ")
    def dispalybike(self):

        print("My bike Engine type :",self.Engine)
        print("My bike Milage:",self.Milage)

objectcar=car()
objectcar.cardetai()
objectcar.display()
objectcar.dispalycar()

objectbike=bike()
objectbike.bikedetai()
objectbike.display()
objectbike.dispalybike()M
