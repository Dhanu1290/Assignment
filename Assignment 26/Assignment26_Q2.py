class Circle:
    # Class variable
    PI = 3.14

    # Constructor
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    # Accept radius from user
    def Accept(self):
        self.Radius = float(input("Enter radius: "))

    # Calculate area
    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    # Calculate circumference
    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    # Display values
    def Display(self):
        print("Radius :", self.Radius)
        print("Area :", self.Area)
        print("Circumference :", self.Circumference)


# Create multiple objects
Obj1 = Circle()
Obj2 = Circle()

# For Object 1
print("Object 1")
Obj1.Accept()
Obj1.CalculateArea()
Obj1.CalculateCircumference()
Obj1.Display()

# For Object 2
print("\nObject 2")
Obj2.Accept()
Obj2.CalculateArea()
Obj2.CalculateCircumference()
Obj2.Display()