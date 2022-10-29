#!/usr/bin/env python3

"""Alta3 | Python Basics | Final Project"""

from random import choice, randint, shuffle
from cryptography.fernet import Fernet


def load_key():

    """ key for encryption """

    with open("key.key", "rb") as file:
        key = file.read()
        return key


key = load_key()
fer = Fernet(key)


def view():

    """ function to view """

    with open("demofile.txt", "r") as pwd_file:
        for line in pwd_file.readlines():
            data = line.rstrip()  # removes trailing characters
            # splitting the data identified by |
            website, email, passwd = data.split('|')
            print("Website: ", website, "|Email: ", email, "| Password: ",
                    fer.decrypt(passwd.encode()).decode())


def add():

    """ function to add """

    lowercase = [
        'a',
        'b',
        'c',
        'd',
        'e',
        'f',
        'g',
        'h',
        'i',
        'j',
        'k',
        'l',
        'm',
        'n',
        'o',
        'p',
        'q',
        'r',
        's',
        't',
        'u',
        'v',
        'w',
        'x',
        'y',
        'z']
    # converts the above list item to upper
    uppercase = [x.upper() for x in lowercase]
    symbols = [
        '!',
        '#',
        '$',
        '%',
        '&',
        '(',
        ')',
        '*',
        '+',
        ',',
        '-',
        '.',
        '/',
        ':',
        ';',
        '<',
        '=',
        '>',
        '?',
        '@',
        '[',
        ']',
        '^',
        '_',
        '`',
        '{',
        '|',
        '}',
        '~']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    password_lowercase = [choice(lowercase) for _ in range(randint(4, 5))]
    password_uppercase = [choice(uppercase) for _ in range(randint(4, 5))]
    password_symbols = [choice(symbols) for _ in range(randint(5, 6))]
    password_numbers = [choice(numbers) for _ in range(randint(4, 5))]
    password_list = password_lowercase + password_uppercase + \
        password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)

    website = input("Website: ")
    email = input("email/username: ")
    if len(website) == 0 or len(email) == 0:
        print("Please make sure not to leave any spaces empty.")
    else:
        with open("demofile.txt", "a") as pwd_file: # saving to the text file in append mode
            pwd_file.write(
                    website +
                    '|' +
                    email +
                    '|' +
                    fer.encrypt(
                        password.encode()).decode() +
                    "\n")


def main():

    """ run the program in a loop """

    while True:
        mode = input(
            "Would to like to view or add passwords? (Enter view, add or quit)").lower()
        if mode == "quit":
            break
        if mode == "add":
            add()
        elif mode == "view":
            view()
        else:
            print("Invalid entry.")
            continue


if __name__ == "__main__":
    main()
