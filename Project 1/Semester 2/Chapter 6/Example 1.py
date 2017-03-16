"""
    Create a Text file
    Populate with numbers 10, 20, 30, 40, 50, 60,70, 80, 90, 100
    Print the contents of the text file
    Add 101, 102, 103, 104, 105 to the list
    Print contents of the file again
"""
file = ''

def ready_file():
    global file
    file = open("file.txt", 'w')        # Create File.txt                                           #1
    file.close()                        # Close File.txt
    file = open("file.txt","r+")        # Open File.txt for reading and writing
    
def read_file(thisFile):
    thisFile.seek(0)  # Move reading to line 0
    print(thisFile.readlines())  # Read all lines of the file                                #3

def write_nums(thisFile, num1, num2, step):
    for num in range(num1, num2+1, step):  # Use a loop to add numbers, in intervals of 'step'      #2,#4
        thisFile.write(str(num) + "\n")
            
            
def main():
    global file
    ready_file()
    write_nums(file,10,100,10)
    read_file(file)
    write_nums(file,101,105,1)
    read_file(file)
    file.close()                        # Final file closing

main()
