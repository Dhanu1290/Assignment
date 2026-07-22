# Accept file names
SourceFile = input("Enter existing file name: ")
DestinationFile = input("Enter new file name: ")

# Copy contents
with open(SourceFile, "r") as src:
    data = src.read()

with open(DestinationFile, "w") as dest:
    dest.write(data)

print("Contents of", SourceFile, "copied into", DestinationFile)