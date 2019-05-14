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
    c = 0
    words = x.split(" ")
    print(words)
    lastWord = words[-1]
    for letters in lastWord:
        c += 1
    print(c)
        
x = "find the last word"
lastWordCount(x)       