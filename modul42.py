# Input x 10
def main():
    x = []
    for i in range(10):
        x.append(int(input()) % 42)
    print(set(x))


# Starting main
main()