import threading

def EvenFactor(num):

    total = 0

    print("Even Factors:")

    for i in range(1, num + 1):
        if (num % i == 0) and (i % 2 == 0):
            print(i, end=" ")
            total += i

    print("\nSum of Even Factors =", total)


def OddFactor(num):

    total = 0

    print("Odd Factors:")

    for i in range(1, num + 1):
        if (num % i == 0) and (i % 2 != 0):
            print(i, end=" ")
            total += i

    print("\nSum of Odd Factors =", total)


def main():

    number = int(input("Enter number: "))

    T1 = threading.Thread(target=EvenFactor, args=(number,))
    T2 = threading.Thread(target=OddFactor, args=(number,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("\nExit from main")


if __name__ == "__main__":
        main()