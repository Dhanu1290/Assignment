# 10. Largest of three numbers
largest = lambda a, b, c: a if a >= b and a >= c else (b if b >= c else c)
print(largest(10, 25, 15))   # 25