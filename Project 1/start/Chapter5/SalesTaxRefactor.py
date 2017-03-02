sTax = .05
cTax = .025
saleAmount = 0.0


def getSale():
    global saleAmount
    """
    global saleAmount
    saleAmount += float(input("Input the amount purchased:\t"))
    """
    run = True
    while run:
        while run:
            place = float(input("Enter item cost:\t"))
            if type(place) is float:
                saleAmount += place
                run = False
            else:
                print("Invalid input")
        run = True
        while run:
            check = input("Would you like to input again?\ny/n\n\t")
            if check == "n":
                print("Total purchase amount (before tax):", saleAmount)
                run = False
            elif check == "y":
                break
            else:
                print("Invalid input")


def getTaxes(state, county):
    global saleAmount
    print("State tax:", state*saleAmount)
    print("County tax:", county*saleAmount)
    print("Total tax amount:", state*saleAmount + county*saleAmount)


def getTotalSale(state, county, sale):
    print("Total sale amount:",saleAmount+(state*saleAmount + county*saleAmount))


def main():
    getSale()
    getTaxes(sTax, cTax)
    getTotalSale(sTax ,cTax, saleAmount)


main()
