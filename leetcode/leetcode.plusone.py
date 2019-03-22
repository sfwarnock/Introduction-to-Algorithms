# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 14:55:48 2019

@author: Scott Warnock
"""

"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.


at digits[-1]:
    if digits[-1] == 9:
        digits[-1] = 0
        digits[-2] += 1
    else:
        digits[-1] += 1

"""

def plusOne(digits):
    
    i = -1
    
    while True:
        if digits[i] == 9:
            digits[i] = 0
            i += 1
        if digits[0] == 9:
            digits.insert(0,1)
            break
        else:
            digits[i] += 1
            break

    print(digits)
    
digits = [9, 9, 8]
plusOne(digits)