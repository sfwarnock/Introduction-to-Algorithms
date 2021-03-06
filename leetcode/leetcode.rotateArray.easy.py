# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 06:35:14 2019

@author: Scott Warnock
"""

"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Note:

    Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
    Could you do it in-place with O(1) extra space?
"""

def rotateArray(a, k):
    assert k > 0, 'k steps must be a positive number, not' + str(k)
    assert k <= len(a), 'k steps is greater than the length of the array' + len(a)
    i = len(a) - k 
    j = a[:i] 
    h = a[i:]
    l = []
    
    if k == len(a):
        for num in a[::-1]:
            l.append(num)
        print(l)
    else:    
        l[0:k] = h
        l[k:] = j
        print(l)
        
a = [1, 2, 3, 4, 5, 6, 7]
k = 7
rotateArray(a,k)