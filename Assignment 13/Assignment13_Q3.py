def CheckPerfect(no):
    sum = 0

    for i in range(1, no):
        if no % i == 0:
            sum = sum + i

    if sum == no:
        print("Perfect Number")
    else:
        print("Not Perfect Number")

num = int(input("Enter number: "))
CheckPerfect(num)