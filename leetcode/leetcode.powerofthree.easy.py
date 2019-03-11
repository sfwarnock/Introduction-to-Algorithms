# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 06:19:03 2019

@author: Scott Warnock
"""

# Given an integer, write a function to determine if it is a power of three.

def powerOfThree(n):
    if n <= 0:
        return False
    
    while n % 3 == 0:
        n = n / 3
    if n == 1:
        return True
    else:
        return False
n = 729
powerOfThree(n)