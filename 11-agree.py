from cs50 import get_string

s = get_string("Enter: ")

# In python char data type doesn't exist
if s == "y" or s == "Y":
    print("Agreed.")
# We can use single cote or double cote
elif s == 'n' or s == 'N':
    print("Not agreed.")

# y or any and permutation of yes (Yes, YES) is allowed
if s.lower() in ["y", "yes"]:
    print("Agreed!")
elif s.lower() in ["n", "no"]:
    print("Not agreed!")
