from functools import reduce

def main():
    nums = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

    FilterData = list(filter(lambda x: 70 <= x <= 90, nums))
    print("List after filter :", FilterData)

    MapData = list(map(lambda x: x + 10, FilterData))
    print("List after map :", MapData)

    ReduceData = reduce(lambda x, y: x * y, MapData)
    print("Output of reduce :", ReduceData)

if __name__ == "__main__":
    main()