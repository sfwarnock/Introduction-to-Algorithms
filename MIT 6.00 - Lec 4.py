# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 06:24:01 2019

@author: Scott Warnock
"""
"""
def sqrt(x):
    """"""Specification: Returns the square root of x, if x is a perfect square.""""""
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
        totLegs = 4 * numPigs + 2 * numChicks
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

barnYard()


def solve1(numLegs, numHeads):
    for numSpiders in range(0, numHeads + 1):
        for numChicks in range(0, numHeads - numSpiders + 1):
            numPigs = numHeads - numChicks
            totLegs = 4 * numPigs + 2 * numChicks + 8 * numSpiders
            if totLegs == numLegs:
                return [numPigs, numChicks, numSpiders]
    return [None, None, None]

def barnYard1():
    heads = int(input('Enter the number of heads: '))
    legs = int(input('Enter the number of legs: '))
    pigs, chickens, spiders = solve1(legs, heads)
    if pigs == None:
        print('There is no solution')
    else:
        print('Number of pigs: ', pigs)
        print('Number of chickens: ', chickens)
        print('Number of spiders: ', spiders)

barnYard1()
"""

def solve2(numLegs, numHeads):
    solutionFound = False
    for numSpiders in range(0, numHeads + 1):
        for numChicks in range(0, numHeads - numSpiders + 1):
            numPigs = numHeads - numChicks
            totLegs = 4 * numPigs + 2 * numChicks + 8 * numSpiders
            if totLegs == numLegs:
                print('Number of Pigs: ', str(numPigs))
                print('Number of Chickens: ', str(numChicks))
                print('Number of Spiders: ', numSpiders)
                solutionFound = True
    if not solutionFound: print('There is no solution.')
    
def barnYard2():
    heads = int(input('Enter the number of heads: '))
    legs = int(input('Enter the number of legs: '))
    pigs, chickens, spiders = solve2(legs, heads)
    if pigs == None:
        print('There is no solution')
    else:
        print('Number of pigs: ', pigs)
        print('Number of chickens: ', chickens)
        print('Number of spiders: ', spiders)

barnYard2()