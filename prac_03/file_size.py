"""
Write a program that asks the user for a filename, then prints the number of lines in that file.
"""


def main():
    file_name = file_name = input("Enter filename: ")
    while file_name != "":
        number_of_lines = count_number_of_lines(file_name)
        if not number_of_lines is None:
            print(f"{file_name} has {number_of_lines} lines.")
        file_name = file_name = input("Enter filename: ")


def count_number_of_lines(file_name):
    number_of_line = 0
    try:
        in_file = open(file_name, "r")
        for line in in_file:
            number_of_line += 1
        in_file.close()
        return number_of_line
    except FileNotFoundError:
        print(f"ERROR: {file_name} does not exist.")
    return None


main()
