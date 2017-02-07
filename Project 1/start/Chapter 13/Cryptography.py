"""Cipher Encrypter and Decrypter"""

file = open('Message', 'r+')
file.seek(0)
if not file.readlines():
    original = ""
    print("\n~~~~~~~~~~~ NO TEXT TO USE ~~~~~~~~~~~\n\n")
else:
    file.seek(0)
    original = file.readline()
file.close()
message = []
message_text = ""
is_readable = True


# Encrypt - Mark Gerges
def encrypt(type):
    if type == "caesar":
        caesar()
    elif type == "tree":
        tree()


# Decrypt - Toby Johnson
def decrypt(type):
    if type == "caesar":
        de_caesar()
    elif type == "tree":
        de_tree()


# Cipher Selection - Anfernee Abad
def select():
    master = True
    while master:
        run = True
        selection = input("What's poppin Jimbo?\n- Encrypt\n- Decrypt\n- Display\n- Modify\n- Quit Program\n")
        if selection == "encrypt":
            while run:
                selection = input("What's poppin Jimbo?\n- Caesar\n- Tree\n- Display Text\n- Return\n- Quit\n")
                if selection == "tree" or selection == "caesar":
                    encrypt(selection)
                    run = False
                elif selection == "display":
                    display()
                    run = False
                elif selection == "return":
                    run = False
                elif selection == "quit":
                    return 0
                else:
                    print("Invalid input, please try again.\n*\n*")
        elif selection == "decrypt":
            while run:
                selection = input("What's poppin Jimbo?\n- Caesar\n- Tree\n- Display Text\n- Return\n- Quit\n")
                if selection == "tree" or selection == "caesar":
                    decrypt(selection)
                    run = False
                elif selection == "display":
                    display()
                    run = False
                elif selection == "return":
                    run = False
                elif selection == "quit":
                    return 0
                else:
                    print("Invalid input, please try again.\n*\n*")
        elif selection == "display":
            display()
        elif selection == "modify":
            mod()
        elif selection == "quit":
            return 0
        else:
            print("Invalid input, please try again.\n*\n*")

# Display file text
def display():
    if not message_text == "" and is_readable:
        print(message_text)
    else:
        print("There is no text to display yet")


# Caesar Shift Creator - Sean Curley
def caesar():
    global original
    global message
    global message_text
    global is_readable
    message.clear()
    message_text = ""
    letter_shift = {}
    letter_set = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']
    placeholder = []
    place = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']
    a_equals = input("What letter do you want to shift 'a' to?\n")
    for i in range(letter_set.index(a_equals)):
        placeholder.append(letter_set[i])
    for i in placeholder:
        letter_set.remove(i)
    letter_set.extend(placeholder)
    for item in range(26):
        letter_shift[item] = letter_set[item]
    for letter in original:
        if letter == 'a':
            message.append(letter_shift.get(0))
        elif letter == 'b':
            message.append(letter_shift.get(1))
        elif letter == 'c':
            message.append(letter_shift.get(2))
        elif letter == 'd':
            message.append(letter_shift.get(3))
        elif letter == 'e':
            message.append(letter_shift.get(4))
        elif letter == 'f':
            message.append(letter_shift.get(5))
        elif letter == 'g':
            message.append(letter_shift.get(6))
        elif letter == 'h':
            message.append(letter_shift.get(7))
        elif letter == 'i':
            message.append(letter_shift.get(8))
        elif letter == 'j':
            message.append(letter_shift.get(9))
        elif letter == 'k':
            message.append(letter_shift.get(10))
        elif letter == 'l':
            message.append(letter_shift.get(11))
        elif letter == 'm':
            message.append(letter_shift.get(12))
        elif letter == 'n':
            message.append(letter_shift.get(13))
        elif letter == 'o':
            message.append(letter_shift.get(14))
        elif letter == 'p':
            message.append(letter_shift.get(15))
        elif letter == 'q':
            message.append(letter_shift.get(16))
        elif letter == 'r':
            message.append(letter_shift.get(17))
        elif letter == 's':
            message.append(letter_shift.get(18))
        elif letter == 't':
            message.append(letter_shift.get(19))
        elif letter == 'u':
            message.append(letter_shift.get(20))
        elif letter == 'v':
            message.append(letter_shift.get(21))
        elif letter == 'w':
            message.append(letter_shift.get(22))
        elif letter == 'x':
            message.append(letter_shift.get(23))
        elif letter == 'y':
            message.append(letter_shift.get(24))
        elif letter == 'z':
            message.append(letter_shift.get(25))
        elif letter == ' ':
            message.append(' ')
    message_text = message_text.join(message)
    is_readable = True
    print("*\nCaesar Shift Encrypted\n*")

# Caesar Decryptor - Sean Curley
def de_caesar():
    global original
    global message_text
    global is_readable
    global message
    local_message = []
    message_text = ""
    letter_shift = {}
    letter_set = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']
    placeholder = []
    place = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']
    a_equals = input("What letter did 'a' shift to?\n")
    for i in range(26-letter_set.index(a_equals)):
        placeholder.append(letter_set[i])
    for i in placeholder:
        letter_set.remove(i)
    letter_set.extend(placeholder)
    for item in range(26):
        letter_shift[item] = letter_set[item]
    for letter in message:
        if letter == "a":
            local_message.append(letter_shift.get(0))
        elif letter == "b":
            local_message.append(letter_shift.get(1))
        elif letter == "c":
            local_message.append(letter_shift.get(2))
        elif letter == "d":
            local_message.append(letter_shift.get(3))
        elif letter == "e":
            local_message.append(letter_shift.get(4))
        elif letter == "f":
            local_message.append(letter_shift.get(5))
        elif letter == "g":
            local_message.append(letter_shift.get(6))
        elif letter == "h":
            local_message.append(letter_shift.get(7))
        elif letter == "i":
            local_message.append(letter_shift.get(8))
        elif letter == "j":
            local_message.append(letter_shift.get(9))
        elif letter == "k":
            local_message.append(letter_shift.get(10))
        elif letter == "l":
            local_message.append(letter_shift.get(11))
        elif letter == "m":
            local_message.append(letter_shift.get(12))
        elif letter == "n":
            local_message.append(letter_shift.get(13))
        elif letter == "o":
            local_message.append(letter_shift.get(14))
        elif letter == "p":
            local_message.append(letter_shift.get(15))
        elif letter == "q":
            local_message.append(letter_shift.get(16))
        elif letter == "r":
            local_message.append(letter_shift.get(17))
        elif letter == "s":
            local_message.append(letter_shift.get(18))
        elif letter == "t":
            local_message.append(letter_shift.get(19))
        elif letter == "u":
            local_message.append(letter_shift.get(20))
        elif letter == "v":
            local_message.append(letter_shift.get(21))
        elif letter == "w":
            local_message.append(letter_shift.get(22))
        elif letter == "x":
            local_message.append(letter_shift.get(23))
        elif letter == "y":
            local_message.append(letter_shift.get(24))
        elif letter == "z":
            local_message.append(letter_shift.get(25))
        elif letter == " ":
            local_message.append(" ")
    message = local_message
    message_text = message_text.join(message)
    is_readable = True
    print("*\nCaesar Shift Decrypted\n*")


# Tree Creator - Anfernee Abad
def tree():
    global original
    global message
    global is_readable
    characters = []
    for letter in original.lower():
        characters.append(letter)
    for i in characters:
        if i == 'a':
            characters[characters.index(i)] = "|"
        elif i == 'b':
            characters[characters.index(i)] = "|\\"
        elif i == 'c':
            characters[characters.index(i)] = "||"
        elif i == 'd':
            characters[characters.index(i)] = "|/"
        elif i == 'e':
            characters[characters.index(i)] = "\\"
        elif i == 'f':
            characters[characters.index(i)] = "||\\"
        elif i == 'g':
            characters[characters.index(i)] = "|||"
        elif i == 'h':
            characters[characters.index(i)] = "||/"
        elif i == 'i':
            characters[characters.index(i)] = "/"
        elif i == 'j':
            characters[characters.index(i)] = "|\\\\"
        elif i == 'k':
            characters[characters.index(i)] = "|\\|"
        elif i == 'l':
            characters[characters.index(i)] = "|\\/"
        elif i == 'm':
            characters[characters.index(i)] = "|/\\"
        elif i == 'n':
            characters[characters.index(i)] = "|/|"
        elif i == 'o':
            characters[characters.index(i)] = "|//"
        elif i == 'p':
            characters[characters.index(i)] = "\\\\"
        elif i == 'q':
            characters[characters.index(i)] = "\\|"
        elif i == 'r':
            characters[characters.index(i)] = "\\/"
        elif i == 's':
            characters[characters.index(i)] = "/\\"
        elif i == 't':
            characters[characters.index(i)] = "/|"
        elif i == 'u':
            characters[characters.index(i)] = "//"
        elif i == 'v':
            characters[characters.index(i)] = "||\\\\"
        elif i == 'w':
            characters[characters.index(i)] = "||//"
        elif i == 'x':
            characters[characters.index(i)] = "|||\\"
        elif i == 'y':
            characters[characters.index(i)] = "|||/"
        elif i == 'z':
            characters[characters.index(i)] = "||||"
    message = characters
    print("*\nTree Code Encrypted\n*")
    is_readable = False


# Tree Decryptor - Anfernee Abad
def de_tree():
    global message
    global message_text
    global is_readable
    letters = []
    for element in message:
        letters.append(element)
    for i in letters:
        if i == '|':
            letters[letters.index(i)] = "a"
        elif i == '|\\':
            letters[letters.index(i)] = "b"
        elif i == '||':
            letters[letters.index(i)] = "c"
        elif i == '|/':
            letters[letters.index(i)] = "d"
        elif i == '\\':
            letters[letters.index(i)] = "e"
        elif i == '||\\':
            letters[letters.index(i)] = "f"
        elif i == '|||':
            letters[letters.index(i)] = "g"
        elif i == '||/':
            letters[letters.index(i)] = "h"
        elif i == '/':
            letters[letters.index(i)] = "i"
        elif i == '|\\\\':
            letters[letters.index(i)] = "j"
        elif i == '|\\|':
            letters[letters.index(i)] = "k"
        elif i == '|\\/':
            letters[letters.index(i)] = "l"
        elif i == '|/\\':
            letters[letters.index(i)] = "m"
        elif i == '|/|':
            letters[letters.index(i)] = "n"
        elif i == '|//':
            letters[letters.index(i)] = "o"
        elif i == '\\\\':
            letters[letters.index(i)] = "p"
        elif i == '\\|':
            letters[letters.index(i)] = "q"
        elif i == '\\/':
            letters[letters.index(i)] = "r"
        elif i == '/\\':
            letters[letters.index(i)] = "s"
        elif i == '/|':
            letters[letters.index(i)] = "t"
        elif i == '//':
            letters[letters.index(i)] = "u"
        elif i == '||\\\\':
            letters[letters.index(i)] = "v"
        elif i == '||//':
            letters[letters.index(i)] = "w"
        elif i == '||//':
            letters[letters.index(i)] = "x"
        elif i == '|||/':
            letters[letters.index(i)] = "y"
        elif i == '||||':
            letters[letters.index(i)] = "z"
    message = letters
    message_text = message_text.join(message)
    print("*\nTree Decrypted\n*")
    is_readable = True


# File Modifier - Toby Johnson
def mod():
    file = open("Message", "r+")
    global original
    run = True
    while run:
        sel = input("What would you like to do with the file?\n- Clear\n- Write\n- Return\n")
        if sel == "clear":
            file.seek(0)
            file.truncate()
            print("*\nFile Cleared\n*")
        elif sel == "write":
            temp = input("What would you like to write to the file?\n")
            file.write(temp)
            print("*\nFile Writtem\n*")
        elif sel == "return":
            original = file.readline(0).lower()
            file.close()
            return 1
        else:
            print("Invalid input, please try again.\n*\n*")


# Main Function - Mark Gerges
def main():
    check = 1
    while check:
        check = select()
    print("\n\n\n\n~~~~~~~~~~~ END OF PROGRAM ~~~~~~~~~~~")


main()
