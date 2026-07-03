# 8. Numbers divisible by both 3 and 5 using filter()
nums = [10, 15, 20, 30, 45, 50]
divisible = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, nums))
print("Divisible by 3 and 5:", divisible)