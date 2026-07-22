# Accept file name from user
FileName = input("Enter file name: ")

# Open file and count words
with open(FileName, "r") as f:
    data = f.read()
    count = len(data.split())

print("Total number of words in", FileName, ":", count)