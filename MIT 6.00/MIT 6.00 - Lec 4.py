# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 06:24:01 2019

@author: Scott Warnock
"""

def sqrt(x):
    """Specification: Returns the square root of x, if x is a perfect square."""
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
    
sqrt(25)


def solve(numLegs, numHeads):
    for numChicks in range(0, numHeads + 1):
        numPigs = numHeads - numChicks
        totLegs = (4 * numbPigs) + (2 * numChicks)
        if totLegs == numLegs:
            return [numPigs, numChicks]
        return [None, None]

def barnYard():
    heads = int(input('Enter the number of heads: '))
    legs = int(input('Enter the number of legs: '))
    pigs, chickens = solve(legs, heads)
    if pigs == None:
        print('There is no solution')
    else:
        print('Number of pigs: ', pigs)
        print('Number of chickens: ', chickens)