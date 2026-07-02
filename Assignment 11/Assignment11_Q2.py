def CountDigits(no):
    count = 0

    while no > 0:
        no = no // 10
        count = count + 1

    print("Number of digits:", count)

num = int(input("Enter number: "))
CountDigits(num)