from functools import reduce

def ChkPrime(num):

    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def main():
    nums = [2, 70, 11, 10, 17, 23, 31, 77]

    FilterData = list(filter(ChkPrime, nums))
    print("List after filter :", FilterData)
    
    MapData = list(map(lambda x: x * 2, FilterData))
    print("List after map :", MapData)

    ReduceData = reduce(lambda x, y: x if x > y else y, MapData)
    print("Output of reduce :", ReduceData)

if __name__ == "__main__":
    main()

