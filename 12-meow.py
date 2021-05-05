# def meow():
#    print("meow")

# for i in range(3):
#    meow()
# If we define meow() below we will get error
# defing meow above the loop will solve that porblem

# Another Approach by defining main()
def main():
    meow(3)

def meow(n):
    for i in range(n):
        print("meow")

# If we dont't call main() nothing will execute
main()