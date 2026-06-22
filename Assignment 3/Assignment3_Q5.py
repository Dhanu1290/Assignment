# Using print()
def addition(a, b):
    print(a + b)

Ret1 = addition(10, 20)
print("Ret1:", Ret1)  
#   ---------------
#Output: 30         #print() displays the result but does not return it to the caller.
# Ret1: None
#----------------

# Using return
def addition(a, b):
    return a + b

Ret2 = addition(10, 20)
print("Ret2:", Ret2)
#----------------
#Output: 30     #return sends the result back to the caller, allowing it to be stored in a variable
#-----------------

