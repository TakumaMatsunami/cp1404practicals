"""
Seminar 3
"""

file_name = input("File Name: ")
filein = open(file_name, "r")
for line in filein:
    if line.startswith("#"):
        print(line)
filein.close()