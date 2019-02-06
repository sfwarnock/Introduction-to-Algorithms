# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 06:34:49 2019

@author: Scott Warnock
"""

#   Input: A sequence of n numbers A = [a1, a2,....an] and a value v.

#   Output: An index i such that v = A[i] or the special value NIL if v does not appear in A.

#   Write pseudocode for linear search, which scans through the sequence, looking for v.
#   Using a loop invariant, prove the your algorithm is correct. Make sure that your
#   loop invariant fullfills the three necessary properties.

def linearSearch(array):
    for arrayValue in range(len(array)):
        if array[arrayValue] == number:
            return print(arrayValue)
    return print(-1);
    
array = [125, 26, 35, 105, 104]
number = 125
linearSearch(array)