import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python program.py <source_file>")
        return

    source_file = sys.argv[1]
    destination_file = "Demo.txt"

    try:
        with open(source_file, "r") as src:
            data = src.read()

        with open(destination_file, "w") as dest:
            dest.write(data)

        print(f"Contents of {source_file} copied to {destination_file}")

    except FileNotFoundError:
        print(f"{source_file} does not exist.")

if __name__ == "__main__":
    main()