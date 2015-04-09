#!/usr/bin/env python3
"""
Magic Trick problem
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
'''Recently you went to a magic show. You were very impressed by one of the tricks, 
so you decided to try to figure out the secret behind it!

The magician starts by arranging 16 cards in a square grid: 4 rows of cards, 
with 4 cards in each row. Each card has a different number from 1 to 16 
written on the side that is showing. Next, the magician asks a volunteer 
to choose a card, and to tell him which row that card is in.

Finally, the magician arranges the 16 cards in a square grid again, 
possibly in a different order. Once again, he asks the volunteer which row her 
card is in. With only the answers to these two questions, the magician then correctly 
determines which card the volunteer chose. Amazing, right?

You decide to write a program to help you understand the magician's technique. 
The program will be given the two arrangements of the cards, and the volunteer's 
answers to the two questions: the row number of the selected card in the first 
arrangement, and the row number of the selected card in the second arrangement. 
The rows are numbered 1 to 4 from top to bottom.

Your program should determine which card the volunteer chose; 
or if there is more than one card the volunteer might have chosen (the magician 
did a bad job); or if there's no card consistent with the volunteer's answers 
(the volunteer cheated).

Solving this problem

Usually, Google Code Jam problems have 1 Small input and 1 Large input. 
This problem has only 1 Small input. Once you have solved the Small input, 
you have finished solving this problem.
'''


_input_file_description = \
'''
Input:
3           -> Number of cases
2           -> Choice for the first arrangement | Start of case
1 2 3 4     |
5 6 7 8     |-> First arrangemet
9 10 11 12  |
13 14 15 16 |
3           -> Choice for the second arrangement
1 2 5 4     |
3 11 6 15   |-> Second arrangemet
9 10 7 12   |
13 14 8 16  | End of case
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

Output:
Case #1: 7
Case #2: Bad magician!
Case #3: Volunteer cheated!
'''

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
  content = open(filename).read().splitlines()  
  
  cases = content[0]
  arrange1 = []
  arrange2 = []

  case = 0
  content.append([1])

  for idx, val in enumerate(content[1:]):
    if(len(val) == 1):
      if(idx%2 == 0):
        if(len(arrange2) == 4):
          selrow1 = set(arrange1[int(choice1)-1])
          selrow2 = set(arrange2[int(choice2)-1])
          card = list(selrow1.intersection(selrow2))
          arrange1 = []
          arrange2 = []
          if (len(card) > 1):
            print("Case #{}: Bad magician!".format(case))
          elif (len(card) < 1):
            print("Case #{}: Volunteer cheated!".format(case))
          else:
            print("Case #{}: {}".format(case,card[0]))
        case = case + 1 
        choice1 = val
      else:
        choice2 = val
    else:
      if(len(arrange1) < 4):
        arrange1.append([int(i) for i in val.split()])
      elif(len(arrange2) < 4):
        arrange2.append([int(i) for i in val.split()])
  return 0


if __name__ == "__main__":
    status = main(parse_args().input_file)
    sys.exit(status)
