# -*- coding: utf-8 -*-
"""
Created on Thu May  9 06:18:11 2019

@author: Scott Warnock
"""

"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""


def lastWordCount(x):
    assert len(x) > 1, 'Length of string too short to contain "last word"'
    
    c = 0
    words = x.split(" ")
    for letters in words[-1]:
        c += 1
    return c
        
x = "count the last word of the sentence"
lastWordCount(x)       