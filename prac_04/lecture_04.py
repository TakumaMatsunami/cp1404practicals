"""
Lecture 4, week 4

Collections of data
    1. List []
        object containing multiple data items
        each item = element, with index (0~)
    2. Tuple
    3. Dictionary
    4. Set
    5. Class
        one that we create by ourselves (done in the following week)

Sequence is an object that contains multiple data elements in order
    for python = lists, tuples, and strings
        lists = mutable
        tuples, and strings = immutable

List
    starts from 0
    from the right end starts from -1
"""

# Write a program that contains a (hard-coded) list of names. Ask the user which name they want to display
# as a number (1 = first name in the list), and then display it. Avoid any IndexError by using exception handling.

names = ["Alex", "Alan", "Alon", "Alba", "Avalon"]
try:
    number = int(input(f"Name (1~{len(names)}): "))
    print(f"Your chosen name is {names[number - 1]}")
except IndexError:
    print("Index Error, invalid input")

