from multiprocessing import Pool
import os

def count_even(n):
    return (os.getpid(), n, n // 2)

if __name__ == "__main__":
    data = [1000000, 2000000, 3000000, 4000000]

    with Pool() as p:
        results = p.map(count_even, data)

    for pid, num, count in results:
        print("Process ID :", pid)
        print("Input Number :", num)
        print("Even Number Count :", count)
        print()