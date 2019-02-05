# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 06:15:53 2019

@author: Scott Warnock
"""

# Rewrite insertion-sort 2.1-1 procedure to sort into nonincreasing instead of nondecreasing order.

def decreasingInsertionSort(theArray):
    
    for arrayIndex in range(-1, len(theArray)):
        