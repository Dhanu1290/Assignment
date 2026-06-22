def fun():
    x = 10
    print(x)

fun()
print(x)

# output : 10
# NameError: name 'x' is not defined

# Inside the function fun(), the variable x = 10 is a local variable.
# It is accessible only inside that function.
#fun() is called → it prints 10 
#print(x) is called outside the function 

# x is not defined globally, so Python throws an error
# Hence: NameError