def DisplayEven(no):
    for i in range(2, no + 1, 2):
        print(i, end=" ")

num = int(input("Enter number: "))
DisplayEven(num)