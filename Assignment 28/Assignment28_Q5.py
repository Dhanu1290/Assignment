# Accept file name and word from user
FileName = input("Enter file name: ")
Word = input("Enter word to search: ")

# Open file and read contents
with open(FileName, "r") as f:
    data = f.read()

# Check if word is present
if Word in data:
    print(Word, "found in", FileName)
else:
    print(Word, "not found in", FileName)