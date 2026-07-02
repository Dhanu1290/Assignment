def Factorial(no):
    fact = 1

    for i in range(1, no + 1):
        fact = fact * i

    print("Factorial is:", fact)

num = int(input("Enter number: "))
Factorial(num)