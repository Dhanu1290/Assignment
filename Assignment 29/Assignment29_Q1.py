import os

def main():
    filename = input("Enter file name: ")

    if os.path.isfile(filename):
        print(f"{filename} exists.")
    else:
        print(f"{filename} does not exist.")

if __name__ == "__main__":
    main()