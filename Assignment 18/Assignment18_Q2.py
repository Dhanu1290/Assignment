def Maximum(arr):
    max_num = arr[0]

    for num in arr:
        if num > max_num:
            max_num = num

    return max_num


def main():
    size = int(input("Enter number of elements: "))

    data = []

    for i in range(size):
        value = int(input())
        data.append(value)

    print("Maximum number:", Maximum(data))


if __name__ == "__main__":
    main()