from cs50 import get_string

people = {
    # key-value pair
    # data type of key and value can differ
    # this type is called dictionary (dict)
    # which is implemented using hash underneath the hood
    "Jakir" : "01721142",
    "Ron" : "09876543",
    "David" : "907833"

}

name = get_string("Name: ")
if name in people:
    print("Number: " + people[name])
else:
    print("Not found.")