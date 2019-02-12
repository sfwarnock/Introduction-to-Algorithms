# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 06:15:11 2019

@author: Scott Warnock
"""

# LeetCode Two Sum

# Given an array of integers, return indices of the two nubmers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

#   given nums = [2, 7, 11, 15], target = 9

#   because nums[0] + nums[1] = 2 + 7 = 9
#   return [0,1]

def sumTwo(numbersArray):
    # Outer Loop moves through array
    for values in range(0,len(numbersArray)):                       # start at index 0 of the array 
        currentArrayValue = numbersArray[values]                    # value of the array = index of array
        targetValue = 9                                             # target value
        # Inner loop adds values until target sum is found.
        while currentArrayValue > 0 and targetSum != targetValue:   # while current array value is greater than zero and target value is not equal to target

numbersArray = [2, 7, 11, 15]
sumTwo(numbersArray)
print(sumTwo)