"""
Random Numbers

print(random.randint(5, 20))  # line 1
What did you see on line 1?
What was the smallest number you could have seen, what was the largest?
    Smallest = 5
    Largest = 20

print(random.randrange(3, 10, 2))  # line 2
What did you see on line 2?
What was the smallest number you could have seen, what was the largest?
Could line 2 have produced a 4?
    Smallest = 3
    Largest = 9
    cant produce 4 due to its step of 2 making the code only to print odd numbers.

print(random.uniform(2.5, 5.5))  # line 3
What did you see on line 3?
What was the smallest number you could have seen, what was the largest?
    Smallest = 2.5000
    Largest = 5.5000

Write code, not a comment, to produce a random number between 1 and 100 inclusive.
"""

from random import uniform


def produce_random_number():
    random_number = uniform(1, 100)
    print(random_number)


produce_random_number()
