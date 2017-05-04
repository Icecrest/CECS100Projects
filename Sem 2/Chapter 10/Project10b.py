# Sean Curley
# 015068363
# Project 10b
# May 1, 2017


class BankAccount:

    def __init__(self):
        self.__balance = 500.00

    def check_bal(self):
        case = str(self.__balance).rpartition('.')
        newbal = ""
        if len(case[2]) < 1:
            place = [case[0], case[1], '00']
            newbal = newbal.join(place)
        elif len(case[2]) == 1:
            place = [case[0], case[1], case[2] + '0']
            newbal = newbal.join(place)
        else:
            newbal = str(self.__balance)

        print("Your balance is", newbal, "\n")

    def deposit(self):
        while 1 == 1:
            amt = input("Enter the amount you would like to deposit:\n~~\t")
            if '.' in amt:
                print("DEBUG found")
                case = amt.rpartition('.')
                print(case)
                try:
                    amt = float(amt)
                except ValueError:
                    print("~~ ValueError Raised ~~\nInvalid amount entered.  Please enter a new amount.")

                if case[2] == '' or amt <= 0 or amt > self.__balance:
                    print("DEBUG error")
                    print("Invalid amount entered.  Please enter a new amount.")
                else:
                    self.__balance += amt
                    print("Amount Deposited\n")
                    break
            else:
                print("Invalid input, please try again.")

    def withdraw(self):
        while 1 == 1:
            amt = input("Enter the amount you would like to withdraw:\n~~\t")
            if "." in amt:
                case = amt.rpartition('.')
                try:
                    amt = float(amt)
                except ValueError:
                    print("~~ ValueError Raised ~~\nInvalid amount entered.  Please enter a new amount.")

                if case[2] == '' or amt <= 0 or amt > self.__balance:
                    print("Invalid amount entered.  Please enter a new amount.")
                else:
                    self.__balance -= amt
                    print("Amount Withdrawn\n")
                    break
            else:
                print("Invalid input, please try again.")


def main():
    balance = 500.0
    account = BankAccount()

    check = 1
    while check == 1:
        print("1: Check Balance\n2: Deposit Funds\n3: Withdraw Funds\n\n0: Exit Program")
        user = input("Enter the corresponding number to the action you would like to take\n~~\t")
        if user == '1':
            account.check_bal()
        elif user == '2':
            account.deposit()
        elif user == '3':
            account.withdraw()
        elif user == '0':
            break
        else:
            print("Invalid input, please try again.\n")

main()