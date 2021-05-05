from cs50 import get_int

x = get_int("x: ")
y = get_int("y: ")

print(x + y)

# input() return string so we have to typecast
# x = input("x: ")
# atoi -> ascii to int
# in python we can typecast string to int
x = int(input("x: "))
y = int(input("y: "))

print(x + y)