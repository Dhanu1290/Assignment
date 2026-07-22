class BankAccount:

    # Class variable
    ROI = 10.5

    # Constructor
    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    # Display account details
    def Display(self):
        print("Account Holder:", self.Name)
        print("Balance:", self.Amount)

    # Deposit amount
    def Deposit(self):
        amt = float(input("Enter deposit amount: "))
        self.Amount += amt
        print("Amount deposited successfully.")

    # Withdraw amount
    def Withdraw(self):
        amt = float(input("Enter withdrawal amount: "))

        if amt <= self.Amount:
            self.Amount -= amt
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance!")

    # Calculate interest
    def CalculateInterest(self):
        return (self.Amount * BankAccount.ROI) / 100


# Create multiple objects
Obj1 = BankAccount("Dhananjay", 50000)
Obj2 = BankAccount("Rahul", 30000)

# Object 1
print("----- Account 1 -----")
Obj1.Display()
Obj1.Deposit()
Obj1.Withdraw()
print("Interest =", Obj1.CalculateInterest())
Obj1.Display()

# Object 2
print("\n----- Account 2 -----")
Obj2.Display()
Obj2.Deposit()
Obj2.Withdraw()
print("Interest =", Obj2.CalculateInterest())
Obj2.Display()