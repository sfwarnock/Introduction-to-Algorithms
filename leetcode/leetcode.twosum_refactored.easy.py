# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 06:54:10 2019
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
    d = {}
    for i in range(len(a)):
        d[i] = a[i]
    print (d)
    
    for k in d:
        if k == 2:
            print (k, d[k])
    
    
target = 22
a = [2, 7, 11, 15]
sumTwo(a, target)