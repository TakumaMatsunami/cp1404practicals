"""
3 method to import module

# import entire thing inside that module the use fully qualified name
import math
math.pi

# import specific function from a module
from math import pi
pi

# import everything, but the module name isnt required
from math import *
pi
"""

# from random import randint
#
# length = int(input("Length: "))
# width = randint(1, length)
# area = length * width
# print(f"Area of {length} x {width} is {area}")

# def print_grid(number_of_rows, number_of_columns):
#     # Version 3
#     print(f"{"*" * number_of_columns}\n" * number_of_rows)
#     # Version 2
#     for row in range(number_of_rows):
#         print("*" * number_of_columns)
#
#
# print_grid(3, 7)

"""import random
from shlex import join


def main():
    name = "Takuma Matsunami"
    print("Menu: ")
    choice = input("> ").upper()
    while choice != "Q":
        if choice == "G":
            name = get_valid_name()
        elif choice == "P":
            print(f"Hello {name}")
        elif choice == "S":
            random_name = get_random_name(name)
            print(f"Hello, secret {random_name}")
        else:
            print("Error")
        choice = input("> ").upper()
    print("Bye")


def get_valid_name():
    name = input("Name: ")
    while name == "":
        print("Invalid Name")
        name = input("Name: ")
    return name


def get_random_name(name):
    random_name = list(name)
    random.shuffle(random_name)
    return "".join(random_name)"""

"""
determine_grade
convert_usd_to_aud
print_report
calculate_average
is_even
get_valid_age
"""


def main():
    print_greeting()


def print_greeting():
    for i in range(5):
        print("Hello")


"""
how to write a good commit message

just like the information in patch notes, release notes
capital first 
this commit will ...
"""

main()
