#!/usr/bin/env python3
"""
Dijkstra problem
for Google Code Jam 2015
Qualification Round

Link to problem description:
https://code.google.com/codejam/contest/6224486/dashboard#s=p2

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
import itertools
import operator
# modules I've written:
from helpful import *
from quatern import *


_program_description = \
'''
The Dutch computer scientist Edsger Dijkstra made many important contributions 
to the field, including the shortest path finding algorithm that bears his name. 
This problem is not about that algorithm.

You were marked down one point on an algorithms exam for misspelling "Dijkstra" 
-- between D and stra, you wrote some number of characters, 
each of which was either i, j, or k. You are prepared to argue to get your 
point back using quaternions, an actual number system (extended from complex numbers) 
with the following multiplicative structure:

|    | 1 | i  | j  | k  |
|----|---|----|----|----|
| 1  | 1 | i  | j  | k  |
| i  | i | -1 | k  | -j |
| j  | j | -k | -1 | i  |
| k  | k | j  | -i | -1 |

To multiply one quaternion by another, look at the row for the first quaternion 
and the column for the second quaternion. For example, to multiply i by j, 
look in the row for i and the column for j to find that the answer is k. 
To multiply j by i, look in the row for j and the column for i to find that the answer is -k.

As you can see from the above examples, the quaternions are not commutative -- that is, 
there are some a and b for which a * b != b * a. However they are associative -- 
for any a, b, and c, it's true that a * (b * c) = (a * b) * c.

Negative signs before quaternions work as they normally do -- for any quaternions a and b,
 it's true that -a * -b = a * b, and -a * b = a * -b = -(a * b).

You want to argue that your misspelling was equivalent to the correct spelling ijk 
by showing that you can split your string of is, js, and ks in two places, 
forming three substrings, such that the leftmost substring reduces 
(under quaternion multiplication) to i, the middle substring reduces to j, 
and the right substring reduces to k. (For example, jij would be interpreted 
as j * i * j; j * i is -k, and -k * j is i, so jij reduces to i.) If this is possible, 
you will get your point back. Can you find a way to do it?
'''


_input_file_description = \
'''
Input

The first line of the input gives the number of test cases, T. T test cases follow. 
Each consists of one line with two space-separated integers L and X, 
followed by another line with L characters, all of which are i, j, or k. 
Note that the string never contains negative signs, 1s, or any other characters. 
The string that you are to evaluate is the given string of L characters repeated X times. 
For instance, for L = 4, X = 3, and the given string kiij, your input string would be kiijkiijkiij.

Output

For each test case, output one line containing "Case #x: y", 
where x is the test case number (starting from 1) and y is either YES or NO, 
depending on whether the string can be broken into three parts 
that reduce to i, j, and k, in that order, as described above.
'''

ideal = ['i', 'j', 'k']

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

def multistances(quarts):
  length = len(quarts)
  if(length%4 == 0):
      return '1'
  elif(length%3 == 0):
    return '-'+quarts[0]
  elif(length%2 == 0):
    return '-1'
  else:
    return quarts[0]

def one_item(mstr):
  for key in sorted(replaces.keys(), reverse=True):
    if key in mstr:
      mstr = mstr.replace(key, replaces.get(key))
  return mstr

def multiply_quartenions(quarts):
  msum = '1'
  if(check_equal(quarts)):
    msum = list(one_item(''.join(quarts)))
  else:
    flist = list(filter(('1').__ne__, quarts))
    # print(flist)
    for q in flist:
      msum = multiply(msum, q)
  return msum

def partition_indices(length, groups, chain = itertools.chain):
  first, middle, last = [0], range(1, length), [length]    
  for div in itertools.combinations(middle, groups-1):
      yield tuple(zip(chain(first, div), chain(div, last)))

def split_list(iterable, groups, chain = itertools.chain):
  omit = {'i' : [], 'j' : [], 'k' : []}
  gmyi = gmyj = [0,0]
  s = iterable if hasattr(iterable, '__getitem__') else tuple(iterable)
  for i,indices in enumerate(partition_indices(len(s), groups, chain)):
    print("possibility: %d" % (i))
    chunk = tuple(s[slice(*x)] for x in indices)
    if(chunk[0] not in omit['i'] and chunk[1] not in omit['j'] and chunk[2] not in omit['k']):
      # print('omit', omit)
      # print('new chunk')
      lmyi = len(chunk[0])
      if(lmyi == gmyi[1]):
        myi = gmyi[0]
      else:
        myi = oversimplify(chunk[0])
      if('i' == myi):
        print('new i')
        gmyi = [myi, lmyi]
        lmyj = len(chunk[1])
        if(lmyj == gmyj[1]):
          myj = gmyj[0]
        else:
          myj = oversimplify(chunk[1])
        if('j' == myj):
          print('new j')
          gmyj = [myj, lmyj]
          myk = oversimplify(chunk[2])
          if('k' == myk):
            return "YES"
          else:
            omit['k'].append(chunk[2])
            # print(chunks)
        else:
          omit['j'].append(chunk[1])
          # print(chunks)
      else:
        omit['i'].append(chunk[0])
        # print(chunks)
  return "NO"

# def split_list(data, n):
#   for splits in combinations(range(1, len(data)), n-1):
#     result = []
#     prev = None
#     for split in chain(splits, [None]):
#         result.append(data[prev:split])
#         prev = split
#     yield result

def half_split(lst):
    half = len(lst)//2
    return lst[:half], lst[half:]

def longest_common_substring(s1, s2):
  m = [[0] * (1 + len(s2)) for i in range(1 + len(s1))]
  longest, x_longest = 0, 0
  for x in range(1, 1 + len(s1)):
      for y in range(1, 1 + len(s2)):
          if s1[x - 1] == s2[y - 1]:
              m[x][y] = m[x - 1][y - 1] + 1
              if m[x][y] > longest:
                  longest = m[x][y]
                  x_longest = x
          else:
              m[x][y] = 0
  return s1[x_longest - longest: x_longest]

def oversimplify(chunk):
  while(len(chunk) > 1):
    prevlen = len(chunk)
    chunk = multiply_quartenions(chunk)
    # print(prevlen, len(chunk),chunk)
  return chunk

def test_combinations(mInput, length):
  if(length < 3):
    return "NO"
  if(length == 3):
    if(mInput == ideal):
      return "YES"
    else:
      return "NO"
  if(check_equal(mInput)):
    return "NO"
  else:
    return split_list(mInput, 3)


def main(filename):
    with open(filename, 'r', encoding='utf-8') as f:
      cases = read_int(f)
      for i in range(cases):
        LX = read_list_of_int(f)
        L = LX[0]
        X = LX[1]
        length = L*X
        mStr = [char for char in read_list_of_char(f)]
        mInput = [item for sublist in [mStr for i in range(X)] for item in sublist]
        print("Case #%d: %s" %(i+1,test_combinations(mInput, length)))

    return 0


if __name__ == "__main__":
    status = main(parse_args().input_file)
    sys.exit(status)
