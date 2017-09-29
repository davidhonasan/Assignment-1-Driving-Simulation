# Checking inputs
def check():
    x = input()
    if x.lower() != "exit":
        x = int(x)
        if x & 1 == 1:
            print("Alice")
            check()
        else:
            print("Bob")
            check()
    else:
        exit()


# Play the function
print("Type \"exit\" to exit.")
check()