"""
Word Occurrences
Estimate: 30 minutes
Actual: 12 minutes
"""
word_to_occurrence = {}

text_line = input("Text: ")
words = text_line.split()
for string in words:
    try:
        word_to_occurrence[string] += 1
    except KeyError:
        word_to_occurrence[string] = 1
longest_word_length = max(len(word) for word in word_to_occurrence)
for word, occurrence in word_to_occurrence.items():
    print(f"{word:{longest_word_length}} : {occurrence}")
