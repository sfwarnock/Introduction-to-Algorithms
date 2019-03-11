# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 06:19:03 2019

@author: Scott Warnock
"""

# Given an integer, write a function to determine if it is a power of three.

def powerOfThree(n):
    m = n
    if m <= 0:
        return False
    
    while m % 3 == 0:
        m = m / 3
    
    if n / 3 == 1:
        print(True)

n = 3
powerOfThree(n)