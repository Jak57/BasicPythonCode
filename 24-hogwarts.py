# import csv
# from cs50 import get_string, get_int

# with open("24-hogwarts.csv", "a") as file:

#     for i in range(8):
#        value = get_int("Id: ")
#        name = get_string("Name: ")
#        writer = csv.writer(file)
#        writer.writerow([value, name])

import csv

# creating dictionary
people = {
        "Jakir" : 0,
        "Jinan" : 0,
        "Shoumik" : 0
}

with open("24-hogwarts.csv") as file:
    # writer function
    reader = csv.reader(file)

    #skips next row
    next(reader)

    # iterate row by row
    # each row is list
    for row in reader:
        key = row[1]
        people[key] += 1

    for key in people:
        print(f"{key}: {people[key]}")
