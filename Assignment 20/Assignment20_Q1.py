import threading

def DisplayEven():
    print("Even Numbers:")
    
    for i in range(2, 21, 2):
        print(i, end=" ")
    
    print()


def DisplayOdd():
    print("Odd Numbers:")
    
    for i in range(1, 20, 2):
        print(i, end=" ")
    
    print()


def main():

    T1 = threading.Thread(target=DisplayEven)
    T2 = threading.Thread(target=DisplayOdd)

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("\nExit from main")

if __name__ == "__main__":
    main()