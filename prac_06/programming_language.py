class ProgrammingLanguage:
    def __init__(self, name, typing, is_reflection, year):
        self.name = name
        self.typing = typing
        self.is_reflection = is_reflection
        self.year = year

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        return False

    def __str__(self):
        return f"{self.name}, {self.typing}, Reflection={self.is_reflection}, First appeared in {self.year}"
