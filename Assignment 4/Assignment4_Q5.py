s = "Python"
print(id(s))

s = s + "3"
print(id(s))

# output : Two different memory addresses
# Strings are immutable,resulting in a change in id()