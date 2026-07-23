import time


FILE_NAME = "sample.txt"   # Change as needed


def read_file():
    try:
        with open(FILE_NAME, "r") as file:
            content = file.read()

            if not content.strip():
                print("File is empty.")
            else:
                print("\n----- File Contents -----")
                print(content)
                print("-------------------------")

    except FileNotFoundError:
        print("Error: File does not exist.")

    except PermissionError:
        print("Error: Permission denied.")

    except OSError:
        print("Error: File cannot be opened.")


def main():
    while True:
        read_file()
        time.sleep(60)  # Wait for 1 minute


if __name__ == "__main__":
    main()