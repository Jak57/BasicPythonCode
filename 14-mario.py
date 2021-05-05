for i in range(3):
    print("#")
# print can take optional named argument, they have name and value
# default value of end is "\0"
for i in range(4):
    print("?", end = "")

print()
# special feature of python
# print ? five time by concatenating
print("?" * 5)

print()

# 3 by 3 grid

for i in range(3):
    for j in range(3):
        #print("#", end = "")
        print("#", end = "")
    print()