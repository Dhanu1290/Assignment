def NameLength(name):
    return len(name)

def main():
    strName = input("Enter name: ")

    result = NameLength(strName)
    print("Length of name is:", result)

if __name__ == "__main__":
    main()