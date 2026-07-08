import threading

def DisplayForward():

    print("Thread1 :")

    for i in range(1, 51):
        print(i, end=" ")

    print()


def DisplayBackward():

    print("Thread2 :")

    for i in range(50, 0, -1):
        print(i, end=" ")

    print()


def main():

    T1 = threading.Thread(target=DisplayForward, name="Thread1")
    T2 = threading.Thread(target=DisplayBackward, name="Thread2")

    T1.start()
    T1.join()      # Wait until Thread1 completes

    T2.start()
    T2.join()

if __name__ == "__main__":
    main()