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
        for j in range(len(a)):
            j = i + 1
            if a[i] + a[j] != target:
                j += 1
            else:
                break
            print(i, a[i], j, a[j]) 
            
target = 6
a = [3, 2, 4]
sumTwo(a, target)