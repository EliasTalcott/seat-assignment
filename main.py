#!/usr/bin/env python3

###
## Call syntax: python3 main.py class_list.xlsx
###

import sys
import random
import excel_text_io

###
## Number of students per table dictionary and algorithm
###
seats = {9: (0, 0, 3, 3, 0, 3, 0), 10: (0, 0, 4, 3, 0, 3, 0), 11: (0, 0, 4, 4, 0, 3, 0),
         12: (3, 0, 3, 3, 0, 3, 0), 13: (4, 0, 3, 3, 0, 3, 0), 14: (4, 0, 4, 3, 0, 3, 0),
         15: (3, 3, 0, 3, 0, 3, 3), 16: (4, 3, 0, 3, 0, 3, 3), 17: (4, 3, 0, 4, 0, 3, 3),
         18: (3, 3, 3, 0, 3, 3, 3), 19: (3, 3, 4, 0, 3, 3, 3), 20: (3, 3, 4, 3, 4, 3, 0),
         21: (3, 3, 3, 3, 3, 3, 3), 22: (3, 3, 4, 3, 3, 3, 3), 23: (3, 4, 4, 3, 3, 3, 3),
         24: (4, 4, 4, 3, 3, 3, 3), 25: (4, 4, 4, 4, 3, 3, 3), 26: (4, 3, 4, 4, 3, 4, 4),
         27: (4, 4, 4, 3, 4, 4, 4), 28: (4, 4, 4, 4, 4, 4, 4)}


def generate_deck(num_students):
    tables = seats[num_students]
    cards = []
    for i, table in enumerate(tables):
        if table == 3:
            cards.append((str(i + 1)) + " of clubs")
            cards.append((str(i + 1)) + " of hearts")
            cards.append((str(i + 1)) + " of spades")
        elif table == 4:
            cards.append((str(i + 1)) + " of clubs")
            cards.append((str(i + 1)) + " of hearts")
            cards.append((str(i + 1)) + " of spades")
            cards.append((str(i + 1)) + " of diamonds")
    return cards


###
## Randomly assign seats
###
def assign_seats(students, cards):
    assignments = {}
    for i, student in enumerate(students):
        num_remaining = len(students) - i
        rand = random.randint(0, num_remaining - 1)
        assignments[student] = cards.pop(rand)
    return assignments


if __name__ == "__main__":
    if len(sys.argv) == 3:
        # Read class list from Excel
        class_list = excel_text_io.read_class_lists(sys.argv[1])
        # Get deck of cards for seating chart
        deck = generate_deck(len(class_list))
        # Assign a random card to each student
        seat_assignments = assign_seats(class_list, deck)
        # Write assignments
        excel_text_io.write_assignments(seat_assignments, sys.argv[2])
    else:
        sys.exit("Wrong arguments!")
