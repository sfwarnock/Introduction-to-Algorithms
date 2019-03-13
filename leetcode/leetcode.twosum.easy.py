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

def sumTwo(a, target):
    
    for i in range(len(a)):
        i = 0
        for j in range(len(a)):
            j = a[i]
            m = target - j
            if m in a:
                print(j, m)
            else:
                i += 1
                
        
            
target = 26
a = [2, 7, 11, 15, 45]
sumTwo(a, target)