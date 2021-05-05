# import get_string function from cs50 library
from cs50 import get_string

answer = get_string("What's your name? ")
print("hello, " + answer);

# Another process using formatted string / F string
answer = get_string("What's your name? ")
print(f"hello, {answer}")

# without importing cs50
answer = input("What's your name? ")
print(f"hello, {answer}")