class Demo:
    # Class variable
    Value = 100

    # Constructor
    def __init__(self, no1, no2):
        self.no1 = no1
        self.no2 = no2

    # Instance method Fun()
    def Fun(self):
        print("Fun() -> no1 =", self.no1, ", no2 =", self.no2)

    # Instance method Gun()
    def Gun(self):
        print("Gun() -> no1 =", self.no1, ", no2 =", self.no2)


# Creating objects
Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)

# Calling methods in the given sequence
Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()