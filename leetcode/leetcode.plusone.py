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

"""

def plusOne(digits):
    if digits[-1] != 9:
        digits[-1] += 1
        print (digits)
        return digits
    
    for digit in range(len(digits),-1):
        if digit == 9:
            digit[:] = 0
    print(digits)
         
digits = [2, 9, 9]
plusOne(digits)