"""
Seminar 04, week 04
"""

# Given a list of names, prompt the user to remove names
# Remove them, until they enter an empty string.
# Ensure the program does not crash when the name is not in the list.

names = ["Ada", "Alan", "Bill", "John"]
print(", ".join(names))
name_to_remove = input("Who do you want to remove? ")
while name_to_remove != "":
    try:
        names.remove(name_to_remove)
    except ValueError:
        print(f"Invalid Name, {name_to_remove} not in list")
    if not names:
        break
    name_to_remove = input("Who do you want to remove? ")
if len(names) != 0:
    print(", ".join(names))
else:
    print("No more names :(")

# Good naming variables
# list of numbers  = numbers
# number of people = number_of_people
# persons age = ages
# tuples containing 2D point data = COORDINATES
# whether person is mutant = is_mutant
# list index = indexes
