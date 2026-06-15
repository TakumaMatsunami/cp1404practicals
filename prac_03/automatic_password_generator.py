"""
Automatic Password Generator

Write a program that asks for a length and what characteristics it must have -
requirements for upper/lower/numeric/special characters - then it should generate a password that matches.
Use your earlier program's checker functionality to validate the generated password.
"""
import random
import string

MIN_LENGTH = 0
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
requirements = ["upper", "lower", "numeric", "special"]
requirement_status = []


def main():
    length = int(input("Length: "))
    for requirement in requirements:
        need_requirement = input(f"Is {requirement} needed (y/n): ").lower()
        requirement_status.append(need_requirement)
    password = generate_valid_password(length)
    while not is_valid_password(password, length, requirement_status):
        password = generate_valid_password(length)
    print(f"Your password is {password}")


def is_valid_password(password, length, requirements_need):
    """Determine if the provided password is valid."""
    # if length is wrong, return False
    if len(password) < MIN_LENGTH or len(password) > length:
        return False
    number_of_lower = 0
    number_of_upper = 0
    number_of_digit = 0
    number_of_special = 0
    for character in password:
        # count each kind of character (use str methods like isdigit)
        if character.islower():
            number_of_lower += 1
        elif character.isupper():
            number_of_upper += 1
        elif character.isdigit():
            number_of_digit += 1
        elif character in SPECIAL_CHARACTERS:
            number_of_special += 1
        pass

    # if any of the 'normal' counts are zero, return False
    if number_of_upper == 0 and requirements_need[0] == "y":
        return False
    if number_of_lower == 0 and requirements_need[1] == "y":
        return False
    if number_of_digit == 0 and requirements_need[2] == "y":
        return False

    # if special characters are required, then check the count of those
    # and return False if it's zero
    if requirements_need[3] == "y":
        if number_of_special == 0:
            return False
    # if we get here (without returning False), then the password must be valid
    return True


def generate_valid_password(length):
    password = ""
    for i in range(length):
        possibility = random.randint(0, 100)
        if possibility <= 25:
            character = random.choice(string.ascii_lowercase)
        elif possibility <= 50:
            character = random.choice(string.ascii_uppercase)
        elif possibility <= 75:
            character = random.choice(SPECIAL_CHARACTERS)
        else:
            character = random.randint(0, 9)
        password += str(character)
    return password


main()
