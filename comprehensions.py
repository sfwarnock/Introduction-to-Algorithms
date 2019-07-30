# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 13:52:08 2019

@author: Scott Warnock
"""

squares = [0, 1, 4, 9, 25]
print(squares)

squaresLoop = []
for num in range(6):
    squaresLoop.append(num*num)
print(squaresLoop)

squaresSingleLine = [num*num for num in range(6)]
print(squaresSingleLine)

#List Comprehensions
even_Squares = []
for num in range(11):
    if num % 2 == 0:
        even_Squares.append(num * num)
print(even_Squares)