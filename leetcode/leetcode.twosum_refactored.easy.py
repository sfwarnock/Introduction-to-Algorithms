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
'''
add array to dict key, value equals index.

k = key[v = 0] - target

while key[v] >= 0:
    if k in d:
        return key[v = 0], k,v
    else:
        key[v + 1]


    d = {a[i]: i for i in range(len(a))}
'''

def sumTwo(a, target):
    d = {}
    
    for i in range(len(a)):
        d[i] = a[i]
    
    j = 0
    k = target - d[j]
    print(k)
    if k in d:
        print('Yes')
    
target = 9
a = [2, 7, 11, 15]
sumTwo(a, target)