# Accept file name from user
FileName = input("Enter file name: ")

# Open file and count lines
with open(FileName, "r") as f:
    count = len(f.readlines())

print("Total number of lines in", FileName, ":", count)