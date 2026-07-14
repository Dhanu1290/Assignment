from multiprocessing import Pool
import time

def calculate_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 5
    return total

def main():
    numbers = [1000000, 2000000, 3000000, 4000000]

    start_time = time.time()

    with Pool() as p:
        results = p.map(calculate_sum, numbers)

    end_time = time.time()

    print("Results:")
    for n, result in zip(numbers, results):
        print(f"N = {n} --> {result}")

    print("\nTotal Execution Time:", end_time - start_time, "seconds")

if __name__ == "__main__":
    main()  