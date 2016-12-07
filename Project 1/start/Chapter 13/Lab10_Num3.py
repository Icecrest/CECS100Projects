"""Cipher Encryptor and Decrypter"""

file = open('Message', 'r+')
file.seek(0)
original = file.readlines().pop(0)
message = []
message_text = ""
is_readable = True


# Encrypt
def encrypt(type):
    if type == "caesar":
        caesar()
    elif type == "tree":
        tree()


# Decrypt
def decrypt(type):
    if type == "caesar":
        de_caesar()
    elif type == "tree":
        de_tree()


# Cipher Selection
def select():
    master = True
    while master:
        run = True
        selection = input("What's poppin Jimbo?\n- Encrypt\n- Decrypt\n- Display\n- Quit Program")
        if selection == "encrypt":
            while run:
                selection = input("What's poppin Jimbo?\n- Caesar\n- Tree\n- Display Text\n- Quit")
                if selection == "tree" or selection == "caesar":
                    encrypt(selection)
                    run = False
                elif selection == "display":
                    display()
                    run = False
                elif selection == "quit":
                    return 0
                else:
                    print("Invalid input, please try again.\n*\n*")
        elif selection == "decrypt":
            while run:
                selection = input("What's poppin Jimbo?\n- Caesar\n- Tree\n- Display Text\n- Quit")
                if selection == "tree" or selection == "caesar":
                    decrypt(selection)
                    run = False
                elif selection == "display":
                    display()
                    run = False
                elif selection == "quit":
                    return 0
                else:
                    print("Invalid input, please try again.\n*\n*")
        elif selection == "display":
            display()
        elif selection == "quit":
            return 0
        else:
            print("Invalid input, please try again.\n*\n*")

# Display file text
def display():
    if not message_text == "":
        if is_readable:
            print(message_text)
    else:
        print("There is no text to display yet")


# Caesar Shift Creator -
def caesar():
    global original
    global message
    global message_text
    global is_readable
    letter_shift = {}
    letter_set = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']
    placeholder = []
    place = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']
    a_equals = input("What letter do you want to shift 'a' to?")
    for i in range(0, letter_set.index(a_equals)):
        placeholder.append(letter_set[i])
        del letter_set[i]
    letter_set.extend(placeholder)
    for item in place:
        letter_shift[item] = letter_set[place.index(item)]
    print(letter_shift)
    """for letter in original:
        if letter == "a":
            message.append(letter_shift.pop(0))
        elif letter == "b":
            message.append(letter_shift.pop(1))
        elif letter == "c":
            message.append(letter_shift.pop(2))
        elif letter == "d":
            message.append(letter_shift.pop(3))
        elif letter == "e":
            message.append(letter_shift.pop(4))
        elif letter == "f":
            message.append(letter_shift.pop(5))
        elif letter == "g":
            message.append(letter_shift.pop(6))
        elif letter == "h":
            message.append(letter_shift.pop(7))
        elif letter == "i":
            message.append(letter_shift.pop(8))
        elif letter == "j":
            message.append(letter_shift.pop(9))
        elif letter == "k":
            message.append(letter_shift.pop(10))
        elif letter == "l":
            message.append(letter_shift.pop(11))
        elif letter == "m":
            message.append(letter_shift.pop(12))
        elif letter == "n":
            message.append(letter_shift.pop(13))
        elif letter == "o":
            message.append(letter_shift.pop(14))
        elif letter == "p":
            message.append(letter_shift.pop(15))
        elif letter == "q":
            message.append(letter_shift.pop(16))
        elif letter == "r":
            message.append(letter_shift.pop(17))
        elif letter == "s":
            message.append(letter_shift.pop(18))
        elif letter == "t":
            message.append(letter_shift.pop(19))
        elif letter == "u":
            message.append(letter_shift.pop(20))
        elif letter == "v":
            message.append(letter_shift.pop(21))
        elif letter == "w":
            message.append(letter_shift.pop(22))
        elif letter == "x":
            message.append(letter_shift.pop(23))
        elif letter == "y":
            message.append(letter_shift.pop(24))
        elif letter == "z":
            message.append(letter_shift.pop(25))
        elif letter == " ":
            message.append(" ")
        """
    message_text = message_text.join(message)
    is_readable = True
    print("*\nCaesar Shift Encrypted\n*")


def de_caesar():
    global message
    global message_text
    global is_readable
    letter_shift = {
        'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j',
        'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't',
        'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z'}
    placeholder = []
    a_equals = input("What letter does 'a' shift to?")
    for i in range(0, letter_shift.index(a_equals)):
        placeholder.append(letter_shift.pop(i))
    for element in placeholder:
        letter_shift.append(element)
    for letter in message_text:
        if letter == "a":
            message.append(letter_shift.pop(0))
        elif letter == "b":
            message.append(letter_shift.pop(1))
        elif letter == "c":
            message.append(letter_shift.pop(2))
        elif letter == "d":
            message.append(letter_shift.pop(3))
        elif letter == "e":
            message.append(letter_shift.pop(4))
        elif letter == "f":
            message.append(letter_shift.pop(5))
        elif letter == "g":
            message.append(letter_shift.pop(6))
        elif letter == "h":
            message.append(letter_shift.pop(7))
        elif letter == "i":
            message.append(letter_shift.pop(8))
        elif letter == "j":
            message.append(letter_shift.pop(9))
        elif letter == "k":
            message.append(letter_shift.pop(10))
        elif letter == "l":
            message.append(letter_shift.pop(11))
        elif letter == "m":
            message.append(letter_shift.pop(12))
        elif letter == "n":
            message.append(letter_shift.pop(13))
        elif letter == "o":
            message.append(letter_shift.pop(14))
        elif letter == "p":
            message.append(letter_shift.pop(15))
        elif letter == "q":
            message.append(letter_shift.pop(16))
        elif letter == "r":
            message.append(letter_shift.pop(17))
        elif letter == "s":
            message.append(letter_shift.pop(18))
        elif letter == "t":
            message.append(letter_shift.pop(19))
        elif letter == "u":
            message.append(letter_shift.pop(20))
        elif letter == "v":
            message.append(letter_shift.pop(21))
        elif letter == "w":
            message.append(letter_shift.pop(22))
        elif letter == "x":
            message.append(letter_shift.pop(23))
        elif letter == "y":
            message.append(letter_shift.pop(24))
        elif letter == "z":
            message.append(letter_shift.pop(25))
    message_text = message_text.join(message)
    is_readable = True
    print("*\nCaesar Shift Decrypted\n*")


# Claw Creator - Sean/Anfernee
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
    print(message)
    print("*\nTree Code Encrypted\n*")
    is_readable = False


# Claw Decryptor - Sean
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


def main():
    check = 1
    while check:
        check = select()
    print("\n\n\n\n~~~~~~~~~~~ END OF PROGRAM ~~~~~~~~~~~")


main()
