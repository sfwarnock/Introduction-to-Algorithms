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
    if n <=0:
        return False

    while n % 2 == 0:
        n = n / 2
        
    return n== 1

n = 16  