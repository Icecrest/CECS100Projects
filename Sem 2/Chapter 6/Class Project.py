# Sean Curley
# 015068363
# Project #7
# Due: 3/22/17

FILE = open('cecs.txt','w')
FILE.close()
# Create and then close the file, if it is not already created

def input_nums():   # Loops until told to end, adding user input number to the file
    file = open('cecs.txt', 'w')
    count = 0
    while count == 0:
        num = input("What number would you like to add to the file?\n\t")
        file.write(num+'\n')
        count = int(input("Enter 0 to enter another number, Enter any other number to end\t"))
    file.close()


def read_file():    # Read the entirety of the file
    file = open("cecs.txt", "r")
    contents = file.read()
    print(contents)
    file.close()


def nextline(file): # Check if the next line fo the file is empty, if not return it
    x = file.readline()
    if x == '':
        return -1
    else: return x


def readlines(file):    # Read using nextline() and multiply the next two numbers in the file
    catch = nextline(file)
    if not catch == -1:
        num1 = int(catch)
        catch = nextline(file)
        if not catch == -1:
            num2 = int(catch)
            return num1*num2
        else:
            print("End of file\n")
            return -1
    else:
        print("End of file\n")
        return -1


def multiply():     # Write the multiplied numbers to the file
    file = open('cecs.txt', 'r+')
    x = 1
    file.seek(0)
    while not x == -1:
        place = readlines(file)
        x = place
        if not x == -1:
            file.write(str(place))
        else: break
    file.close()


def main():
    input_nums()
    read_file()
    multiply()
    read_file()
    print("~~~ END OF PROGRAM ~~~")


main()
