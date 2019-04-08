# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 06:24:01 2019

@author: Scott Warnock
"""

def sqrt(x):
    ans = 0
    
    if x >= 0:
        while ans*ans < x:
            ans = ans + 1
        if ans * ans != x:
            print('x is not a perfect square')
            return None
        else:
            print(ans)
    else: 
        print ('x is a negative number')
        return None
    
sqrt(16)

