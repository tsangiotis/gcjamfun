#!/usr/bin/env python3
"""
Standing Ovation problem
for Google Code Jam 2015
Qualification Round

Link to problem description:
https://code.google.com/codejam/contest/6224486/dashboard

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
'''
It's opening night at the opera, and your friend is the prima donna (the lead female singer). 
You will not be in the audience, but you want to make sure she receives 
a standing ovation -- with every audience member standing up and clapping their hands for her.

Initially, the entire audience is seated. Everyone in the audience has a shyness level. 
An audience member with shyness level Si will wait until at least S other 
audience members have already stood up to clap, and if so, she will immediately 
stand up and clap. If Si = 0, then the audience member will always stand up and 
clap immediately, regardless of what anyone else does. For example, 
an audience member with Si = 2 will be seated at the beginning, 
but will stand up to clap later after she sees at least two other people standing and clapping.

You know the shyness level of everyone in the audience, 
and you are prepared to invite additional friends of the prima donna 
to be in the audience to ensure that everyone in the crowd stands up and claps in the end. 
Each of these friends may have any shyness value that you wish, not necessarily the same. 
What is the minimum number of friends that you need to invite to guarantee a standing ovation?
'''


_input_file_description = \
'''
Input

The first line of the input gives the number of test cases, T. T test cases follow. 
Each consists of one line with Smax, the maximum shyness level of the 
shyest person in the audience, followed by a string of Smax + 1 single digits. 
The kth digit of this string (counting starting from 0) represents how many 
people in the audience have shyness level k. For example, the string "409" would mean
that there were four audience members with Si = 0 and nine audience members with 
Si = 2 (and none with Si = 1 or any other value). Note that there will initially 
always be between 0 and 9 people with each shyness level.

The string will never end in a 0. Note that this implies that there will always
be at least one person in the audience.

Output

For each test case, output one line containing "Case #x: y", 
where x is the test case number (starting from 1) and y is the minimum number of friends you must invite.
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
  with open(filename, 'r', encoding='utf-8') as f:
    cases = read_int(f)
    for i in range(cases):
      case = read_list_of_str(f)
      Smax = int(case[0])
      people = [int(char) for char in str(case[1])]

      clapping = 0
      added = 0

      for idx, p in enumerate(people):
        toadd = 0
        if(idx == 0):
          clapping = p
        else:
          while(clapping+toadd < idx and p > 0):
            added += 1
            toadd += 1
          clapping += p+toadd
      print('Case #%d: %d' %(i+1, added))
      

  return 0


if __name__ == "__main__":
  status = main(parse_args().input_file)
  sys.exit(status)
