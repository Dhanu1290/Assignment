def Minimum(arr):
    min_num = arr[0]

    for num in arr:
        if num < min_num:
            min_num = num

    return min_num


def main():
    size = int(input("Enter number of elements: "))

    data = []

    for i in range(size):
        value = int(input())
        data.append(value)

    print("Minimum number:", Minimum(data))


if __name__ == "__main__":
    main()