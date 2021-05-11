import csv
from cs50 import get_string

# with open("23-phonebook.csv", "a") as file
# using above syntax we don't have to close file
# but have to indent codes below

file = open("23-phonebook.csv", "a")

name = get_string("Name: ")
number = get_string("Number: ")

writer = csv.writer(file)
# using list in writerow function
writer.writerow([name, number])

file.close()