# sys -> system library of python
from sys import argv

if len(argv) == 2:
    print("Hello, " + argv[1])
else:
    print("Hello, world")

# print all command line argument
for arg in argv:
    print(arg)