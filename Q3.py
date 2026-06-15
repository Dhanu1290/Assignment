#is value returned by id() same for 2 variable holding the same value?
#Answer: Not always

a = 10
b = 10
c = [10]
d = [10]

print(id(a))  # same memory
print(id(b))  # same memory
print(id(c))  # separate memory
print(id(d))  # separate memory