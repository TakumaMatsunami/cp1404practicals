"""
write a program that asks the user for a password, with error-checking to repeat if the password doesn't meet a minimum length set by a variable.
"""


def main():
    password = get_password()
    print_starts(password)


def get_password():
    password = input("Password: ")
    while password == "":
        print("No empty")
        password = input("Password: ")
    return password


def print_starts(password):
    for character in password:
        print("*", end="")


main()
