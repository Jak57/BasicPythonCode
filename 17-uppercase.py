from cs50 import get_string

# print("Before: ", end = "")
s = get_string("Before: ")

t = s.upper();
print(f"After: {t}")

# Another approach
for c in s:
    print(c.upper(), end = "")

print()