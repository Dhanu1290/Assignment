def Frequency(arr, num):
    count = 0

    for value in arr:
        if value == num:
            count += 1

    return count


def main():
    size = int(input("Enter number of elements: "))

    data = []

    for i in range(size):
        value = int(input())
        data.append(value)

    search = int(input("Enter element to search: "))

    print("Frequency:", Frequency(data, search))


if __name__ == "__main__":
    main()