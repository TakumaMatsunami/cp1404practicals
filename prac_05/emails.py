"""
Word Occurrences
Estimate: 30 minutes
Actual: 18 minutes
"""
name_to_email = {}

email = input("Email: ")
while email != "":
    name = email.split("@")
    name = name[0].split(".")
    for i, word in enumerate(name):
        name[i] = name[i].title()
    name = " ".join(name)
    is_name = input(f"Is your name {name}? (Y/n) ").lower()
    if is_name == "y" or is_name == "":
        name_to_email[name] = email
    else:
        name = input("Name: ")
        name_to_email[name] = email
    email = input("Email: ")
print()

for name, email in name_to_email.items():
    print(f"{name} ({email})")
