from sys import getsizeof

value = input("Enter a value: ")

print("Value is:", value)
print("Data type:", type(value))
print("Memory address:", id(value))
print("Size in bytes:", getsizeof(value))