from multiprocessing import Pool
from math import factorial
import os

def calculate_factorial(n):
    return (os.getpid(), n, factorial(n))

if __name__ == "__main__":
    data = [10, 15, 20, 25]

    with Pool() as p:
        results = p.map(calculate_factorial, data)

    for pid, num, fact in results:
        print("Process ID :", pid)
        print("Input Number :", num)
        print("Factorial :", fact)
        print()