# main program
def main():
        z = input()
        x = list(z)
        ball = 1
        if z.lower() != "exit":
            while x:
                y = x.pop(0)
                if y.lower() == "a":  # If input A
                    if ball == 1:  # Checking ball location
                        ball = 2
                    elif ball == 2:
                        ball = 1
                elif y.lower() == "b":  # If input B
                    if ball == 2:  # Checking ball location
                        ball = 3
                    elif ball == 3:
                        ball = 2
                elif y.lower() == "c":  # If input C
                    if ball == 3:  # Checking ball location
                        ball = 1
                    elif ball == 1:
                        ball = 3
            print("The ball is at cup no. " + str(ball))
            main() # looping program
        else:
            exit()


# starting program
print("Welcome to cups and ball. To exit, type \"exit\"")
main()