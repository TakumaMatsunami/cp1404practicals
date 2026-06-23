"""
Intermediate Exercises
"""

COLOR_TO_CODE = {"charcoal": "#36454f", "cadet blue": "#5f9ea0", "dark salmon": "#e9967a", "dark sea green": "	#8fbc8f",
                  "frostbite": "#e936a7", "green lizard": "#a7f432", "harlequin": "#3fff00", "heliotrope": "#df73ff",
                  "honolulu blue": "#006db0", "international orange": "#ff4f00"}

color_name = input("Color Name: ").lower()
while color_name != "":
    try:
        print(f"The code for color {color_name:5} is {COLOR_TO_CODE[color_name]}")
    except KeyError:
        print("Invalid Color")
    color_name = input("Color Name: ").lower()


