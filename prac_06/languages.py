from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
java = ProgrammingLanguage("Java", "Static", True, 1995)
c_plus = ProgrammingLanguage("C++", "Static", False, 1983)

programing_languages = [python, ruby, visual_basic, java, c_plus]

print("The dynamically typed languages are:")
for programing in programing_languages:
    if programing.is_dynamic():
        print(programing.name)
