def main():
    filename = input("Enter file name: ")

    try:
        with open(filename, "r") as file:
            print("File Contents:")
            print(file.read())
    except FileNotFoundError:
        print(f"{filename} does not exist.")

if __name__ == "__main__":
    main()