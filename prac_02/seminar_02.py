
def main():
    lower_boundary = int(input("Lower Boundary: "))
    higher_boundary = int(input("Higher Boundary: "))
    while lower_boundary >= higher_boundary:
        print("Error")
        higher_boundary = int(input("Higher Boundary: "))


