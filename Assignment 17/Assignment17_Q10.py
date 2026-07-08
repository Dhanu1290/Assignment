def SumDigits(num):
    total = 0

    while num > 0:
        digit = num % 10
        total += digit
        num //= 10

    return total

def main():
    number = int(input("Enter number: "))
    print("Sum of digits:", SumDigits(number))

if __name__ == "__main__":
    main()