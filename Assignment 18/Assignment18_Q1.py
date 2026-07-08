def SumList(arr):
    total = 0

    for num in arr:
        total += num

    return total


def main():
    size = int(input("Enter number of elements: "))

    data = []

    for i in range(size):
        value = int(input())
        data.append(value)

    print("Sum:", SumList(data))


if __name__ == "__main__":
    main()