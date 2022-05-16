# write your code here

import sys

a = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
print("-------------------")
print("|", a[0], a[1], a[2], "|")
print("|", a[3], a[4], a[5], "|")
print("|", a[6], a[7], a[8], "|")
print("-------------------")


def number_or_not(x, y):
    if not x.isnumeric() or not y.isnumeric():
        print("You should enter numbers!")


def bigger_smaller(x, y):
    if (x > 3 or x < 1) or (y > 3 or y < 1):
        print("Coordinates should be from 1 to 3!")


def is_occupied(x):
    if a[x] != " ":
        print("This cell is occupied! Choose another one!")


for t in range(10):
    coordinates = list(input("Enter the coordinates: "))
    while (not coordinates[0].isnumeric()) or (not coordinates[2].isnumeric()):
        number_or_not(coordinates[0], coordinates[2])
        coordinates = list(input("Enter the coordinates: "))
    row = int(coordinates[0])
    column = int(coordinates[2])
    while bigger_smaller(row, column):
        coordinates = list(input("Enter the coordinates: "))
        number_or_not(coordinates[0], coordinates[2])
        row = int(coordinates[0])
        column = int(coordinates[2])
        bigger_smaller(row, column)
    nr = 0
    nr_of_X = [x for x in a if x == "X"]
    nr_of_0 = [o for o in a if o == "O"]
    empty_spaces = sum(x.count(" ") for x in a)
    for i in range(1, 4):
        for j in range(1, 4):
            if i == row and j == column:
                while (not coordinates[0].isnumeric()) or (not coordinates[2].isnumeric()):
                    number_or_not(coordinates[0], coordinates[2])
                    coordinates = list(input("Enter the coordinates: "))
                row = int(coordinates[0])
                column = int(coordinates[2])
                while bigger_smaller(row, column):
                    coordinates = list(input("Enter the coordinates: "))
                    number_or_not(coordinates[0], coordinates[2])
                    row = int(coordinates[0])
                    column = int(coordinates[2])
                    bigger_smaller(row, column)
                if a[nr] == " ":
                    if t % 2 == 0:
                        a[nr] = "X"
                    elif t % 2 == 1:
                        a[nr] = "O"

                    print("-------------------")
                    print("|", a[0], a[1], a[2], "|")
                    print("|", a[3], a[4], a[5], "|")
                    print("|", a[6], a[7], a[8], "|")
                    print("-------------------")
                elif a[nr] != " ":
                    is_occupied(nr)
                    coordinates = list(input("Enter the coordinates: "))
                    row = int(coordinates[0])
                    column = int(coordinates[2])
                    is_occupied(nr)
            nr = nr + 1

        if (a[0] == a[1] == a[2]) or (a[0] == a[3] == a[6]):
            if a[0] == "O":
                sys.exit(print("O wins"))
            elif a[0] == "X":
                sys.exit(print("X wins"))
        elif (a[2] == a[5] == a[8]) or (a[6] == a[7] == a[8]):
            if a[8] == "O":
                sys.exit(print("O wins"))
            elif a[8] == "X":
                sys.exit(print("X wins"))
        elif (a[4] == a[3] == a[5]) or (a[4] == a[1] == a[7]) or (a[4] == a[0] == a[8]) or (a[4] == a[2] == a[6]):
            if a[4] == "O":
                sys.exit(print("O wins"))
            elif a[4] == "X":
                sys.exit(print("X wins"))
        elif (nr_of_0 == 5 and nr_of_X == 4) or (nr_of_0 == 4 and nr_of_X == 5) or empty_spaces == 0:
            sys.exit(print("Draw"))
