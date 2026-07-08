import threading

def Maximum(arr):
    print("Maximum Element :", max(arr))

def Minimum(arr):
    print("Minimum Element :", min(arr))

def main():

    size = int(input("Enter number of elements: "))

    data = []

    for i in range(size):
        value = int(input())
        data.append(value)

    t1 = threading.Thread(target=Maximum, args=(data,))
    t2 = threading.Thread(target=Minimum, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()