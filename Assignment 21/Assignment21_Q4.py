import threading
from functools import reduce

SumResult = 0
ProductResult = 0

def SumList(arr):

    global SumResult

    SumResult = sum(arr)


def ProductList(arr):

    global ProductResult

    ProductResult = reduce(lambda x, y: x * y, arr)


def main():

    size = int(input("Enter number of elements: "))

    data = []

    for i in range(size):
        value = int(input())
        data.append(value)

    t1 = threading.Thread(target=SumList, args=(data,))
    t2 = threading.Thread(target=ProductList, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum =", SumResult)
    print("Product =", ProductResult)

if __name__ == "__main__":
    main()