"""
Word Occurrences
Estimate: 40 minutes
Actual: 18 minutes
"""
from itertools import count

TEXT_FILE = "wimbledon.csv"


def main():
    country_to_champion = read_files()
    display_champion(country_to_champion)
    display_country(country_to_champion)


def read_files():
    country_to_champion = {}
    with open(TEXT_FILE, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        things = [line.split(",") for line in in_file]
    for thing in things:
        if thing[1] in country_to_champion:
            country_to_champion[thing[1]][1] += 1
        else:
            country_to_champion[thing[1]] = [thing[2], 1]
    return country_to_champion


def display_champion(country_to_champion):
    print("Wimbledon Champions: ")
    for champion in country_to_champion.values():
        print(f"{champion[0]} {champion[1]}")
    print()


def display_country(country_to_champion):
    print(f"These {len(set(country_to_champion))} countries have won Wimbledon: ")
    print(", ".join(set(country_to_champion)))


main()
