from cs50 import get_int

def main():
    i = get_positive_int()
    print(i)

def get_positive_int():

    # in python scope isn't a problem in function
    # all variables are accessible inside function
    # but not outside
    while True:
        n = get_int("Enter: ")
        if (n > 0):
            break
    return n

main()
