a = 10
b = 10               #integers are immutable

print(id(a)==id(b))  # True, because small integers are cached & reused by Python
