"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
WORD_FORMAT = "cv"

# User input
word_format = input("Word format: ").lower()
# Random
word_format = ""
for i in range(5):
    word_format += random.choice(WORD_FORMAT)

word = ""
for kind in word_format:
    if kind == "c" or "%":
        word += random.choice(CONSONANTS)
    elif kind == "*":
        probability = random.randint(0, 100)
        if probability <= 50:
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)
    else:
        word += random.choice(VOWELS)

print(word)
