is_valid_input = False
while not is_valid_input:
    try:
        age = int(input("Age: "))
        if age < 0:
            print("Age m"
                  "ust be >= 0")
        else:
            is_valid_input = True
    except ValueError:

        print("Invalid (not an integer)")

