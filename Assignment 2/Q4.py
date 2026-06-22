#memory size is different for different data types, because of value,characters,number of elements etc.


from sys import getsizeof


a = 10
b = "Hello"
c = [1,2,3]

print(getsizeof(a))
print(getsizeof(b))
print(getsizeof(c)) 