# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 06:15:53 2019

@author: Scott Warnock
"""

# Rewrite insertion-sort 2.1-1 procedure to sort into nonincreasing instead of nondecreasing order.

def decreasingInsertionSort(theArray):
    
    for arrayIndex in range(1, len(theArray)):
        
        currentArrayValue = theArray[arrayIndex]
        position = arrayIndex
        
        while position > 0 and theArray[position - 1] < currentArrayValue:
            theArray[position] = theArray[position - 1]
            position = position - 1
            
        theArray[position] = currentArrayValue

theArray = [31, 41, 59, 26, 41, 58, 1, 14, 100, 123, 145]
decreasingInsertionSort(theArray)
print(theArray)