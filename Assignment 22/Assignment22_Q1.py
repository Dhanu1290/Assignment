from multiprocessing import Pool

def sum_of_squares(n):
    return sum(i * i for i in range(1, n + 1))

def main():
    numbers = [1000000, 2000000, 3000000, 4000000]

    with Pool() as p:
        result = p.map(sum_of_squares, numbers)

    print(result)

if __name__ == "__main__":
    main()