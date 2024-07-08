# TODO
from cs50 import get_int


def main():
    while True:
        height = get_int('Height: ')

        if height >= 1 and height <= 8:
            break  # Exit the loop if the height is valid
        else:
            print("Height must be a positive integer between 1 and 8.")

    for i in range(1, height + 1):
        print(" " * (height - i) + "#" * i)


main()
