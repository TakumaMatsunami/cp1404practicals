"""
1. Write code that asks the user for their name, then opens a file called name.txt
    and writes that name to it. Use open and close for this question.

2. In the same file, but as if it were a separate program, write code that opens
    "name.txt" and reads the name (as above) then prints (note the exact output),

3. Create a text file called numbers.txt and save it in your prac directory.
    Put the following three numbers on separate lines in the file and save it:

4. Now write a fourth block of code that prints the total for all lines in numbers.txt.
    This should work for a file with any number of numbers. Use with instead of open and close for this question.
"""

# Q1
FILENAME = "name.txt"
user_name = input("Name: ")
out_file = open(FILENAME, "w")
print(f"{user_name}", file=out_file)
out_file.close()

# Q2
FILENAME = "name.txt"
in_file = open(FILENAME, "r")
user_name = in_file.read().strip()
in_file.close()
print(f"Hello {user_name}!")

# Q3
FILENAME = "numbers.txt"
with open(FILENAME, "r") as in_file:
    number = 0
    for i in range(2):
        number += int(in_file.readline())
    print(number)

# Q4
FILENAME = "numbers.txt"
with open(FILENAME, "r") as in_file:
    number = 0
    for line in in_file:
        number += int(line)
    print(number)