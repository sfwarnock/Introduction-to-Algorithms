# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 06:16:07 2019

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
    
    word = []
    
    for words in s:
        if words != ' ':
            word.append(words)
    print(word)
    
s = "reverse this string"
reverseWords(s)