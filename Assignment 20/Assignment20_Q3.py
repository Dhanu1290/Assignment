import threading

def EvenList(arr):

    even_sum = 0

    print("Even Elements:")

    for num in arr:
        if num % 2 == 0:
            print(num, end=" ")
            even_sum += num

    print("\nSum of Even Elements =", even_sum)


def OddList(arr):

    odd_sum = 0

    print("\nOdd Elements:")

    for num in arr:
        if num % 2 != 0:
            print(num, end=" ")
            odd_sum += num

    print("\nSum of Odd Elements =", odd_sum)


def main():

    size = int(input("Enter number of elements: "))

    data = []

    for i in range(size):
        value = int(input())
        data.append(value)

    T1 = threading.Thread(target=EvenList, args=(data,))
    T2 = threading.Thread(target=OddList, args=(data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("\nExit from main")


if __name__ == "__main__":
    main()