#!/usr/bin/env python3
"""
Ominous Omino problem
for Google Code Jam 2015
Qualification Round

Link to problem description:
https://code.google.com/codejam/contest/6224486/dashboard#s=p3

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
    #                                        default=False, help='show progress')
    args = parser.parse_args()
    return args


def examine(X,R,C):
    if((R*C)%X > 0):  #it cannot be filled
        return "RICHARD"

    if(R == 1 and C == 1):
        if(X in [1]):
            return "GABRIEL"
        else:
            return "RICHARD"

    if((R == 1 and C == 2) or (R == 2 and C == 1)):
        if(X in [1,2]):
            return "GABRIEL"
        else:
            return "RICHARD"
    
    if((R == 1 and C == 3) or (R == 3 and C == 1)):
        if(X in [1]):
            return "GABRIEL"
        else:
            return "RICHARD"
    
    if((R == 1 and C == 4) or (R == 4 and C == 1)):
        if(X in [1,2]):
            return "GABRIEL"
        else:
            return "RICHARD"
    
    if(R == 2 and C == 2):
        if(X in [1,2]):
            return "GABRIEL"
        else:
            return "RICHARD"
    
    if((R == 2 and C == 3) or (R == 3 and C == 2)):
        if(X in [1,2,3]):
            return "GABRIEL"
        else:
            return "RICHARD"
    
    if((R == 2 and C == 4) or (R == 4 and C == 2)):
        if(X in [1,2]):
            return "GABRIEL"
        else:
            return "RICHARD"
    
    if((R == 3 and C == 3)):
        if(X in [1,3]):
            return "GABRIEL"
        else:
            return "RICHARD"
    
    if((R == 3 and C == 4) or (R == 4 and C == 3)):
        if(X in [1,2,3,4]):
            return "GABRIEL"
        else:
            return "RICHARD"
    
    if((R == 4 and C == 4)):
        if(X in [1,2,4]):
            return "GABRIEL"
        else:
            return "RICHARD"

def main(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        cases = read_int(f)
        for i in range(cases):
            case = read_list_of_int(f)
            X = case[0]
            R = case[1]
            C = case[2]

            print("Case #%d: %s" % (i+1, examine(X,R,C)))
    return 0


if __name__ == "__main__":
    status = main(parse_args().input_file)
    sys.exit(status)
