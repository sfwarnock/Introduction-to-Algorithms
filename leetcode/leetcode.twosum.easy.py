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

'''
Pseudocode

Brute Force

for j = 0 to nums.length
    num1 = j[0]
    num2 = j[1]
    
    
    
    
    
Single Pass Hash Table    
    
    myHash = {}
    for index, value in enumerate(nums):
        if target - value in myHash:
            return [myHash[target-value], index]
        myHash[value] = index


'''

def sumTwo(numbersArray):
    # Outer Loop moves through array
    for values in range(0,len(numbersArray)):                       # start at index 0 of the array 
        currentArrayValue = numbersArray[indexValue]                # value of the array = index of array
        targetSum = 9

        # Inner loop adds values until target sum is found.
        for currentArrayValue in numbersArray:                            # while current array value is greater than zero and target value is not equal to target
            

numbersArray = [2, 7, 11, 15]
sumTwo(numbersArray)
print(sumTwo)