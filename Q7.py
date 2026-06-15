# input() returns a string because input is taken as text. To convert it, use typecasting functions like int().
x = input("Enter a number: ")
print(type(x))

x = int(input("Enter a number: "))  #Convert to integer
print(type(x))