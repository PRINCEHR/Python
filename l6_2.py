
class Vechile(object):
    def __init__(self, make, year, model):
        self.make = make
        self.year = year
        self.model = model


    def display(self):
        print("Make :" +self.make)
        print("Model :" +self.model)
        print("Year :" +self.year)

class Ecar(Vechile):
    def __init__(self, BatteryPower, EnginePower, RunTime, Dimension, Seating):
        self.BatterPower = BatteryPower
        self.EnginePower = EnginePower
        self.RunTime = RunTime
        self.Dimension = Dimension
        self.Seating = Seating

    def display(self):
        print("Battery Power:" +self.BatterPower)
        print("Engine Power:" +self.EnginePower)
        print("Run Time: " +self.RunTime)
        print("Dimension: " +self.Dimension)
        print("Seating:" +self.Seating)


objEcar = Ecar('220','229hp','1.2s','3d','4')
objEcar.display()
objVec = Vechile("BMW","2017","X Series")
objVec.display()