def SumDigits(no):
    sum = 0

    while no > 0:
        digit = no % 10
        sum = sum + digit
        no = no // 10

    print("Sum of digits:", sum)

num = int(input("Enter number: "))
SumDigits(num)