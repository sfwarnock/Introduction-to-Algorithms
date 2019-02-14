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

def twoSum(self, nums, target):
    i=0
   l=[0]*2
   for x in nums:
       j=nums.index(x)+1
       for y in nums:
           if(j<len(nums)):
               if (x + nums[j]) == target:
                   l[0]=nums.index(x)
                   l[1]=j
                   break;
                 j=j+1
        return(l) 
    
Single Pass Hash Table    
    
    myHash = {}
    for index, value in enumerate(nums):
        if target - value in myHash:
            return [myHash[target-value], index]
        myHash[value] = index

My code:

for num in array:
    num = array[j]
    i = j + 1
    k = array[j + 1]
    



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