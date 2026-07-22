# Accept file name from user
FileName = input("Enter file name: ")

# Open file and display line by line
with open(FileName, "r") as f:
    for line in f:
        print(line, end="")