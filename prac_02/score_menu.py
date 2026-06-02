"""
Score Menu
"""
from score import determine_grade

MENU_STRING = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    score = 0
    print(MENU_STRING)
    choice = get_valid_choice()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            grade = determine_grade(score)
            print(f"User score {score} is {grade}")
        elif choice == "S":
            print_stars(score)
        choice = get_valid_choice()
    print("Bye")


def get_valid_choice():
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            return "G"
        elif choice == "P":
            return "P"
        elif choice == "S":
            return "S"
        else:
            print("Invalid Choice")
        choice = input(">>> ").upper()
    return "Q"


def get_valid_score():
    score = int(input("Score (0-100): "))
    while score > 100 or score < 0:
        print("Invalid Score")
        score = int(input("Score (0-100): "))
    return score


def print_stars(score):
    for i in range(score):
        print("*", end="")


main()
