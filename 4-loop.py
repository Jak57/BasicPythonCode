
# Infinite loop

while True:
    print("Hello, world")

i = 0
# while loop

while i < 5:
    print("Hello, world")
    i += 1

# for loop
print()
for i in [0, 1, 2, 3]:
    print("Hello, world")

# Another approach: for loop
print()
# range() start from 0 upto 2
for i in range(3):
    print("Hi Jakir")

# Python doesn't support do while loop
# Approach for implement that facility

value = 5
while True:
    if value == 10:
        break
    else:
        # Casting string to int
        value = int(input("Enter value: "))
