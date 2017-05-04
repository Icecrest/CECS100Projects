def exponential(base, power):
    if power > 0:
        return base * exponential(base, power - 1)
    elif base == 0 and power == 0:
        print("Break out the L'Hospital Rule fam")
    elif power == 0:
        return 1
    else:
        pass


def main():
    while 1 == 1:
        try:
            base = float(input("Enter a number as a base:\t"))
            power = int(input("Enter a number to be a power:\t"))
        except ValueError:
            print("Invalid input, try again\n")
        else:
            if power < 0:
                print("Cannot handle a negative value, Please enter again\n")
            else:
                print("Answer is:", exponential(base, power))
                try:
                    check = input("\nEnter 1 to run again, else enter 0\t")
                    check = int(check)
                except ValueError:
                    print("Invalid input entered, try again\n")
                else:
                    if check == 0:
                        break


main()
