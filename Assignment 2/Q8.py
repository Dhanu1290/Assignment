# input() returns a string because input is taken as text. To convert it, use typecasting functions like int().
x = input("Enter a number: ")
print(type(x))


# The output is <class 'str'> because input() returns a string. Python treats all user input as text by default.