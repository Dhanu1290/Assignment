# 6. Minimum element using reduce()
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
minimum = reduce(lambda x, y: x if x < y else y, numbers)
print("Minimum:", minimum)