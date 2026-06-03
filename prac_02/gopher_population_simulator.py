"""
Gopher Population Simulator
"""
from random import randint

TOTAL_YEARS = 10


def main():
    population = 1000
    print("Welcome to the Gopher Population Simulator!")
    print(f"Starting Population: {population}")
    print("Year 1")
    for i in range(2, TOTAL_YEARS + 1):
        print()
        number_of_birth = calculate_birth(population)
        number_of_death = calculate_death(population)
        growth_rate = number_of_birth - number_of_death
        population += growth_rate
        print(f"{number_of_birth:.0f} gophers were born. {number_of_death:.0f} died.")
        print(f"Population: {population:.0f}")
        print(f"Year {i}")


def calculate_birth(population):
    birth_rate = randint(10, 20) / 100
    number_of_birth = population * birth_rate
    return number_of_birth


def calculate_death(population):
    death_rate = randint(5, 25) / 100
    number_of_death = population * death_rate
    return number_of_death


main()
