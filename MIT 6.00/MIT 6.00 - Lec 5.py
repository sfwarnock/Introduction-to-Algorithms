# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 06:13:36 2019

@author: Scott Warnock
"""

#b = 2**999
#print(b)

#x = 0.1
#print(x)

"""
s = 0.0
for i in range(10):
    s += 0.1
    print(s)
"""
    
import math
a = math.sqrt(2)
print(a)


def squareRootBi(x, epsilon):
    """Assumes x >= 0 and epsilon = 0
        Return y s.t. y*y is within epsilion of x"""
    assert x >= 0, 'x must be non-negative, not' + str(x)
    assert epsilon > 0, 'epsilon must be positive, not' + str(epsilon)
    low = 0
    high = x
    ctr = 1
    while abs(guess**2 - x) > epsilon and ctr <= 100:
        print('low:', low, 'high:', high, 'guess:', guess)
        if guess**2 < x:
            low = guess
        else:
            high = guess
        guess = (low + high)/2.0
        ctr += 1
    assert ctr <= 100, 'Iteration count exceeded'
    print ('Bi method. Num. interations:', ctr, 'Estimate:', guess)
    return guess