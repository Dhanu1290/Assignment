def main():
    filename = input("Enter file name: ")
    search_string = input("Enter string to search: ")

    try:
        with open(filename, "r") as file:
            content = file.read()

        count = content.count(search_string)

        print(f'"{search_string}" appears {count} time(s) in {filename}.')

    except FileNotFoundError:
        print(f"{filename} does not exist.")

if __name__ == "__main__":
    main()