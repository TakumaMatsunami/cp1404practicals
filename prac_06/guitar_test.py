from guitar import Guitar

gibson = Guitar("Gibson", 1922, 16035.40)
another_guitar = Guitar("New Brand", 2017, 15000.00)

# Gibson L-5 CES get_age() - Expected 104. Got 104
print(gibson.get_age())

# Another Guitar get_age() - Expected 9. Got 9
print(another_guitar.get_age())

# Gibson L-5 CES is_vintage() - Expected True. Got True
print(gibson.is_vintage())

# Another Guitar is_vintage() - Expected False. Got False
print(another_guitar.is_vintage())
