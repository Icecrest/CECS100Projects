# Sean Curley
# 015068363
# Project #8
# Due 4.12.2017

def main():
    check = 1
    num_list = []
    total = 0
    run = True
    while not check == 0:
        num_sequence = input("Enter a sequence of numbers without spaces:\t")   # Get input of a sequence
        try:
            print("You entered the sequence", num_sequence)
            for i in num_sequence:
                num_list.append(int(i))                                         # Attempt conversion
            print("You entered the sequence", num_sequence)
            print(num_list)
        except ValueError:                                                      # Catch ValueError
            print("\n\n** Conversion raised a ValueError **\n\n")
        except TypeError:                                                       # Catch TypeError
            print("\n\n** Covnversion raised a TypeError **\n\n")
        else:
            print("\n\n* Conversion Successful **\n\n")
            for i in num_list:
                total += i                                                      # Place sequence into total
            print("The sum of all numbers entered is", str(total) + ".")        # Print total
        while run:
            try:
                check = int(input("\n\n1:\tContinue\n0:\tEnd Program"))         # Check for re-run
            except Exception as error:
                print("\n\n** Invalid input, please enter again **\n\n")        # Validate re-run input
            run = False
    print("~~ PROGRAM END ~~")

main()
