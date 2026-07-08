def Add(a, b):
    return a + b

def Sub(a, b):
    return a - b

def Mult(a, b):
    return a * b

def Div(a, b):
    return a / b

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Addition =", Add(num1, num2))
    print("Subtraction =", Sub(num1, num2))
    print("Multiplication =", Mult(num1, num2))
    print("Division =", Div(num1, num2))
    
if __name__ == "__main__":
    main()