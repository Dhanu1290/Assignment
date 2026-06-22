d = {1: "One", 1: "ONE", 2: "Two"}
print(d)

# output : {1: 'ONE', 2: 'Two'}
# Keys must be unique in a dictionary. If you try to create a dictionary with duplicate keys, the last value will overwrite the previous value for that key. In this case, the key 1 is duplicated, and the value "ONE" overwrites the previous value "One". Therefore, the resulting dictionary contains only one entry for the key 1, which is {1: 'ONE', 2: 'Two'}.