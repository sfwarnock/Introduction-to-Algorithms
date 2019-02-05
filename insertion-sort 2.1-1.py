# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 06:06:16 2019

@author: Scott Warnock
"""

# Pseudocode
# insertion-sort(A)
#  for j = 2 to A.length
#   key = A[j]
#   // Insert A[j] into the sorted squence A[1..j - 1]
#   i = j - 1
#   while i > 0 and A[i] > key
#       A[i+1] = A[i]
#       i = i - 1
#   A[i + 1] = key

# O(n^2)

def insertionSort(theArray):
       for arrayIndex in range(1,len(theArray)):    # start at index location 1 of theArray (outer loop)
        
        subArray = theArray[arrayIndex]    # save key value 
        position = arrayIndex                       # find position where value fits
        
        while position > 0 and theArray[position -1] > subArray:   # (inner loop) shift items to the right during
            theArray[position] = theArray[position - 1]                     #
            position = position - 1                                         #
            
        theArray[position] = subArray      # copy value into place
        
theArray = [31, 41, 59, 26, 41, 58, 1, 14, 100, 123, 145]
insertionSort(theArray)
print(theArray)