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
    for values in range(0,len(numbersArray)):       
        currentArrayValue = numbersArray[values]
        targetSum = numbersArray + currentArrayValue
        targetValue = 9
                  
        while currentArrayValue > 0 and targetSum != targetValue:
            if targetSum == targetValue:
                return currentArrayValue[values] and numbersArray[values]
            elif targetSum != targetValue:
                currentArrayValue =+ 1
            
numbersArray = [4, 5, 9, 10, 11]
sumTwo(numbersArray)
print(sumTwo)