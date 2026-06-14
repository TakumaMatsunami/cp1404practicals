"""
"Quick Pick" Lottery Ticket Generator

Write a program that asks the user how many "quick picks" they wish to generate.
The program then generates that many lines of output. Each line consists of 6 random numbers between 1 and 45.
"""
from random import randint

number_of_pick = int(input("How many quick picks? "))
for i in range(number_of_pick):
    for j in range(6):
        number = randint(1, 45)
        print(f"{number:2}", end=" ")
    print()
