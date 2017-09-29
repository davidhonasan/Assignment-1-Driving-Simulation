# KMP
def kmp():
    x = input()
    if x.lower() == "exit":
        exit()
    else:
        stack = x.split("-")  # Splitting
        for i in stack:
            print(i.upper()[0][0], end="")
        print("")
        kmp()


# Starting main
print("Type \"Exit\" to exit the program.")
kmp()