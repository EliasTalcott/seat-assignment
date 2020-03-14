#!/usr/bin/env python3

###
## Call syntax: python3 main.py class_list.xlsx
###

import sys
import random
import excel_io

CLUBS = 0
DIAMONDS = 1
HEARTS = 2
SPADES = 3

if __name__ == "__main__":
    if len(sys.argv) == 2:
        class_list = excel_io.read_class_lists(sys.argv[1])
        print(class_list)
    else:
        sys.exit("Wrong arguments!")
