def ReverseDisplay(no):
    for i in range(no, 0, -1):
        print(i, end=" ")

num = int(input("Enter number: "))
ReverseDisplay(num)