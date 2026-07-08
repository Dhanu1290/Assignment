def CountDigits(num):
    count = 0

    while num > 0:
        count += 1
        num //= 10

    return count

def main():
    number = int(input("Enter number: "))
    print("Number of digits:", CountDigits(number))

if __name__ == "__main__":
    main()