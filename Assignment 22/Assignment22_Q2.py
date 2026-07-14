from multiprocessing import Pool
from math import factorial
import os

def calculate_factorial(num):
    return (os.getpid(), num, factorial(num))

def main():
    numbers = [10, 15, 20, 25]

    with Pool() as p:
        results = p.map(calculate_factorial, numbers)

    print("Process ID\tInput Number\tFactorial")
    for pid, num, fact in results:
        print(f"{pid}\t\t{num}\t\t{fact}")

if __name__ == "__main__":
    main()