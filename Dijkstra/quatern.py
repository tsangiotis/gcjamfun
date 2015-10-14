"""
Something to help with the quaternion operations.

Author: 
  Tasos Sangiotis
  (tsagi)

Language:
  Python 3(.4)

Date:
  April, 2015
"""

__name__ = 'quatern'
__all__  = ['multiply', 'replaces']

mult = [
[ '1',  'i',  'j',  'k', '_', 'I', 'J', 'K'],
[ 'i', '_',  'k', 'J', 'I',  '1', 'K',  'j'],
[ 'j', 'K',  '_',  'i', 'J',  'k',  '1', 'I'],
[ 'k',  'j', 'I', '_', 'K', 'J',  'i',  '1'],
['_', 'I', 'J', 'K',  '1',  'i',  'j',  'k'], 
['I',  '1', 'K',  'j',  'i', '_',  'k', 'J'], 
['J',  'k',  '1', 'I',  'j', 'K', '_',  'i'], 
['K', 'J',  'i',  '1',  'k',  'j', 'I', '_']
]

p = {'1': 0, 'i': 1, 'j': 2, 'k':3, '_': 4, 'I': 5, 'J': 6, 'K':7 }
replaces = {'iiii': '1', 'jjjj': '1','kkkk': '1','iii': 'I' ,'jjj': 'J',
'kkk': 'K','ii': '_' ,'jj': '_','kk': '_'}

def multiply(q1, q2):
	return mult[p[q1]][p[q2]]