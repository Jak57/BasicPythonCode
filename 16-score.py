from cs50 import get_int
# score = [70, 90, 40]
score = []

# taking input from user and adding to list score
for i in range(3):
    score.append(get_int("score: "))

# can't concatenate string with float
# print("Average: " + (sum(score) / len(score)))

print("Average: " + str(sum(score) / len(score)))
print(f"Average: {sum(score) / len(score)}")

average = sum(score) / len(score)
print(f"Average: {average}")

