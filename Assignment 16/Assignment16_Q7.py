def CheckDivisible(no):
    if no % 5 == 0:
        return True
    else:
        return False

def main():
    num = int(input("Enter number: "))

    result = CheckDivisible(num)
    print(result)

if __name__ == "__main__":
    main()