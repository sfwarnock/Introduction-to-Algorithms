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

a = [31, 41, 59, 26, 41, 58]

def insertionSort(a):
    
    for currentCard in a:
        cardKey = currentCard[1]
        arrayIndex = currentCard - 1
        while arrayIndex > 0 and a[arrayIndex] > cardKey:
            a[arrayIndex + 1] = a[arrayIndex]
            arrayIndex =+ 1
        a[arrayIndex + 1] = cardKey

insertionSort(a)