import cs50
# can use comma for importing multiple functions
#from cs50 import get_string, get_int

# if don't use from cs50 import get_string then have to use (.)
name = cs50.get_string("What's your name? ")
print("Hi, " + name)

number = input("Number: ")
print("Value: " + number)