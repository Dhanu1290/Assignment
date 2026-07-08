def Add(no1, no2):
    return no1 + no2

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = Add(num1, num2)
    print("Output:", result)

if __name__ == "__main__":
    main()