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



def insertionSort(theArray):
       for arrayIndex in range(1,len(theArray)):
        
        currentArrayValue = theArray[arrayIndex]
        position = arrayIndex
        
        while position > 0 and theArray[position -1] > currentArrayValue:
            theArray[position] = theArray[position - 1]
            position = position - 1
            
        theArray[position] = currentArrayValue
        
theArray = [31, 41, 59, 26, 41, 58]
insertionSort(theArray)
print(theArray)