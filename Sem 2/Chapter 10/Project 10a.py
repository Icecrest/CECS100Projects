"""
Create a Bank account class using anything but classes
"""

def main():
    balance = 500.0

    check = 1
    while check == 1:
        print("1: Check Balance\n2: Deposit Funds\n3: Withdraw Funds\n\n0: Exit Program")
        user = input("Enter the corresponding number to the action you would like to take\n~~\t")
        if user == '1':
                                                # Begin Check function
            case = str(balance).rpartition('.')
            newbal = ""
            if len(case[2]) < 1:
                place = [case[0], case[1], '00']
                newbal = newbal.join(place)
            elif len(case[2]) == 1:
                place = [case[0], case[1], case[2] + '0']
                newbal = newbal.join(place)
            else:
                newbal = str(balance)

            print("Your balance is", newbal, "\n")
        elif user == '2':
                                                # Begin Withdraw Function
            while 1 == 1:
                amt = input("Enter the amount you would like to deposit:\n~~\t")
                case = amt.rpartition('.')
                try:
                    amt = float(amt)
                except ValueError:
                    print("~~ ValueError Raised ~~\nInvalid amount entered.  Please enter a new amount.")
                if len(case[2]) == 2 or not case[0] == '' or amt >= 0 or float(amt) > self.__balance:
                    print("Invalid amount entered.  Please enter a new amount.")
                else:
                    balance += amt
                    break
        elif user == '3':
                                                # Begin Deposit function
            while 1 == 1:
                amt = input("Enter the amount you would like to withdraw:\n~~\t")
                case = amt.rpartition('.')
                try:
                    amt = float(amt)
                except ValueError:
                    print("~~ ValueError Raised ~~\nInvalid amount entered.  Please enter a new amount.")
                if len(case[2]) == 2 or not case[0] == '' or amt >= 0 or float(amt) > self.__balance:
                    print("Invalid amount entered.  Please enter a new amount.")
                else:
                    balance -= amt
                    break
        elif user == '0':
            check = 0
        else:
            print("Invalid input, please try again.\n")


main()
