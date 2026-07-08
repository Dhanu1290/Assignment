from functools import reduce

def main():
    nums = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

    FilterData = list(filter(lambda x: x % 2 == 0, nums))
    FilterData = list(filter(lambda x: x % 2 == 0, nums))
    print("List after filter :", FilterData)

    MapData = list(map(lambda x: x ** 2, FilterData))
    print("List after map :", MapData)

    ReduceData = reduce(lambda x, y: x + y, MapData)
    print("Output of reduce :", ReduceData)

if __name__ == "__main__":
    main()