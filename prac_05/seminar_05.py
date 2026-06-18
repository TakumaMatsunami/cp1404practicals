"""
Seminar 5, Week 5
"""

def convert_list_to_dictionary(strings):
    string_to_length = {}
    for string in strings:
        length_of_string = len(string)
        string_to_length[string] = length_of_string
    return string_to_length
