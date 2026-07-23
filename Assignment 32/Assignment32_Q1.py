import os
import time
from datetime import datetime


def create_file():
    now = datetime.now()

    filename = now.strftime("File_%d_%m_%Y_%H_%M_%S.txt")

    with open(filename, "w") as file:
        file.write(f"Filename: {filename}\n")
        file.write(f"Creation Date: {now.strftime('%d-%m-%Y')}\n")
        file.write(f"Creation Time: {now.strftime('%H:%M:%S')}\n")

    print(f"Created: {filename}")


def main():
    while True:
        create_file()
        time.sleep(60)  # Wait 1 minute


if __name__ == "__main__":
    main()