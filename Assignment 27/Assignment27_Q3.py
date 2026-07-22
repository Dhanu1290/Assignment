class Numbers:

    # Constructor
    def __init__(self, Value):
        self.Value = Value

    # Check if number is prime
    def ChkPrime(self):
        if self.Value < 2:
            return False

        for i in range(2, int(self.Value ** 0.5) + 1):
            if self.Value % i == 0:
                return False

        return True

    # Check if number is perfect
    def ChkPerfect(self):
        total = 0

        for i in range(1, self.Value):
            if self.Value % i == 0:
                total += i

        return total == self.Value

    # Display all factors
    def Factors(self):
        print("Factors:", end=" ")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    # Return sum of factors
    def SumFactors(self):
        total = 0

        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                total += i

        return total


# Create objects
Obj1 = Numbers(6)
Obj2 = Numbers(17)

# Object 1
print("Number =", Obj1.Value)
print("Prime :", Obj1.ChkPrime())
print("Perfect :", Obj1.ChkPerfect())
Obj1.Factors()
print("Sum of Factors :", Obj1.SumFactors())

# Object 2
print("\nNumber =", Obj2.Value)
print("Prime :", Obj2.ChkPrime())
print("Perfect :", Obj2.ChkPerfect())
Obj2.Factors()
print("Sum of Factors :", Obj2.SumFactors())