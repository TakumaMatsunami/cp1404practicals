"""
CP1404/CP5632 - Practical
Program to determine score status
"""
from random import randint

def main():
    user_score = float(input("Enter score: "))
    user_grade = determine_grade(user_score)
    print(f"User score {user_score} is {user_grade}")
    if user_grade == "Excellent":
        print("You get a prize!")
    random_score = get_random_score()
    random_grade = determine_grade(random_score)
    print(f"Random: {random_score} = {random_grade}")


def determine_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def get_random_score():
    return randint(0, 100)





main()