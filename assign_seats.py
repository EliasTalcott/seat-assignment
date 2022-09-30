#!/usr/bin/env python
"""
Read class rosters from a CSV and generate random seating arrangements
"""

import csv
import random
import sys
from datetime import datetime


class Roster:
    """Store rosters and assign seats"""
    def __init__(self, infile: str, outfile: str) -> None:
        self.assignments = dict()
        with open(infile, "r", encoding="utf-8") as file:
            self.rosters = {item[0]: list(item[1:]) for item in zip(*list(csv.reader(file)))}
        self.max_roster_len = max(len(item) for item in self.rosters.values())
        self.outfile = outfile

    def assign_seats(self) -> None:
        """Assign each student a seat"""
        for period, students in self.rosters.items():
            real_students = list(filter(str, students))
            self.assignments[period] = random.sample(real_students, len(real_students))
            self.assignments[period] += [""] * (self.max_roster_len - len(real_students))

    def write_assignments(self) -> None:
        """Write seat assignments to CSV"""
        with open(self.outfile, "w", encoding="utf-8") as file:
            writer = csv.writer(file, lineterminator="\n")
            writer.writerow(self.assignments.keys())
            for i in range(self.max_roster_len):
                writer.writerow([self.assignments[key][i] for key in self.assignments])


def main() -> None:
    """Make seat assignments and output to CSV"""
    if len(sys.argv) != 2:
        sys.exit("Roster CSV input is required.")
    roster = Roster(infile=sys.argv[1],
                    outfile=f"{datetime.today().strftime('%Y-%m-%d')}_SeatAssignments.csv")
    roster.assign_seats()
    roster.write_assignments()


if __name__ == "__main__":
    main()
