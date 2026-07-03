# 7. Strings having length greater than 5 using filter()
words = ["Python", "Java", "Programming", "Code", "Lambda"]
long_words = list(filter(lambda x: len(x) > 5, words))
print("Length > 5:", long_words)