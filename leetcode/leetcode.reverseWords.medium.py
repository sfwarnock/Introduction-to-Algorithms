# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 06:30:23 2019

@author: Scott Warnock

Given an input string, reverse the string word by word.

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"

Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:

Input: "a good example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

"""

def reverseWords(s):
    for words in s:
        t = s.split()
        u = t[::-1]
        x = str(' ')
        v = x.join(u)
    print(v)

s = "reverse this string"
reverseWords(s)