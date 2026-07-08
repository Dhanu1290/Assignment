import threading

def ChkPrime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def Prime(arr):
    print("Prime Numbers:")
    for num in arr:
        if ChkPrime(num):
            print(num, end=" ")
    print()


def NonPrime(arr):
    print("Non Prime Numbers:")
    for num in arr:
        if not ChkPrime(num):
            print(num, end=" ")
    print()


def main():
    data = [2, 7, 10, 11, 15, 17, 21]

    t1 = threading.Thread(target=Prime, args=(data,))
    t2 = threading.Thread(target=NonPrime, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()