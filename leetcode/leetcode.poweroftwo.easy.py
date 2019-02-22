# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 06:11:28 2019

@author: Scott Warnock
"""

"""
Given an integer, write a function to determine if it is a power of two.

Example 1:
    Input: 1
    Output: true
    Explanation: 2^0 = 1
    
Example 2:
    Input: 16
    Output: true
    Explanation: 2^4 = 16
    
Example 3:
    Input: 218
    Output: false
    
"""

def powerOfTwo(n):
    m = n
    if m <=0:
        return False

    while m % 2 == 0:
        m = m / 2

    if m == 1:
        print(n, 'is a power of two.')
        return True
    else:
        print(n, 'is not a power of two')
        return False

n = 218
powerOfTwo(n)