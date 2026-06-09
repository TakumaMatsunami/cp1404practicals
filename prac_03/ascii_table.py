"""
Mr. Black the school teacher wants an educational program for his school students to explore the details of ASCII. He wants the app to allow a student to input a character and see the corresponding ASCII code, and vice versa. A sample run of the program should look like (where g and 100 are user inputs):
"""
MINIMUM_NUMBER = 33
MAXIMUM_NUMBER = 127

character_reference = MINIMUM_NUMBER
number_of_column = int(input("How many columns: "))
number_of_row = (MAXIMUM_NUMBER - MINIMUM_NUMBER) // number_of_column

for row in range(number_of_row):
    for column in range(number_of_column):
        print(f"{character_reference:>3}  {chr(character_reference)}", end="  ")
        character_reference += 1
    print()
while character_reference != MAXIMUM_NUMBER:
    character_reference += 1
    print(f"{character_reference:>3}  {chr(character_reference)}", end="  ")
print()

input_character = input("Enter a character: ")
ascii_for_character = ord(input_character)
print(f"The ASCII code for {input_character} is {ascii_for_character}")

number = int(input(f"Enter a number between {MINIMUM_NUMBER} and {MAXIMUM_NUMBER}: "))
while number > MAXIMUM_NUMBER or number < MINIMUM_NUMBER:
    print(f"number have to be between {MINIMUM_NUMBER}-{MAXIMUM_NUMBER}")
    number = int(input(f"Enter a number between {MINIMUM_NUMBER} and {MAXIMUM_NUMBER}: "))
number_character = chr(number)
print(f"The character for {number} is {number_character}")
