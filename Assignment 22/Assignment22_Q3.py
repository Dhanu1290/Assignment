from multiprocessing import Pool

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

def count_primes(n):
    count = 0

    for i in range(2, n + 1):
        if is_prime(i):
            count += 1

    return count

def main():
    numbers = [10000, 20000, 30000, 40000]

    with Pool() as p:
        results = p.map(count_primes, numbers)

    for n, count in zip(numbers, results):
        print(f"Prime numbers between 1 and {n} = {count}")

if __name__ == "__main__":
    main()