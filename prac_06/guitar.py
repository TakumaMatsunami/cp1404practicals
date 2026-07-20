CURRENT_YEAR = 2026
VINTAGE_AGE = 50


class Guitar:

    def __init__(self, name="", produced_year=0, cost=0.00):
        self.name = name
        self.produced_year = produced_year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.produced_year}) : ${self.cost}"

    def get_age(self):
        return CURRENT_YEAR - self.produced_year

    def is_vintage(self):
        return self.get_age() >= VINTAGE_AGE
