#!/usr/bin/env python3
"""
Minesweeper Master problem
for Google Code Jam 2014
Qualification Round

Link to problem description:
https://code.google.com/codejam/contest/dashboard?c=2974486

Author: 
  Tasos Sangiotis
  (tsagi)

Language:
  Python 3(.4)

Date:
  April, 2015

Usage:
  python3 main.py input_file
"""


import sys
import argparse
# modules I've written:
from helpful import *


_program_description = \
'''TEMPLATE PROGRAM DESCRIPTION'''


_input_file_description = \
'''TEMPLATE INPUT FILE DESCRIPTION'''


def parse_args():
    """
    Parse the command line arguments and return them in a namespace.
    """
    parser = argparse.ArgumentParser(description=_program_description)
    parser.add_argument('input_file', help=_input_file_description)
    #parser.add_argument('-v', '--verbose', action='store_true', 
    #                    default=False, help='show progress')
    args = parser.parse_args()
    return args


def main(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        num = read_int(f)
        for i in range(0,num):
          case = read_list_of_int(f)
          R = case[0]   #Rows
          C = case[1]   #Columns 
          M = case[2]   #Mines

          N = R * C - M
          Minefield = [['*' for x in range(R)] for x in range(C)] 
          print(Minefield)
          if(N == 1):
            print("Case #%d:")
            Minefield[0][0] = '.'
            print(Minefield)

    return 0


if __name__ == "__main__":
    status = main(parse_args().input_file)
    sys.exit(status)
