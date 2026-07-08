def ChkPrime(num):

    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def ListPrime(arr):
    total = 0

    for num in arr:
        if ChkPrime(num):
            total += num

    return total


def main():

    size = int(input("Enter number of elements: "))

    data = []

    for i in range(size):
        value = int(input())
        data.append(value)

    print("Sum of prime numbers:", ListPrime(data))


if __name__ == "__main__":
    main()