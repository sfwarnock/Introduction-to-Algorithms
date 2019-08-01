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
    #Loop
even_Squares = []
for num in range(11):
    if num % 2 == 0:
        even_Squares.append(num * num)
print(even_Squares)

    #Comprehension
odd_Squares = [num * num for num in range(11) if num % 2 != 0]
print(odd_Squares)

#More Examples
pythagoreanTriplet = [(a, b, c) for a in range(1,30) for b in range(1,30) for c in range(1,30) if a**2 + b**2 == c**2]
print(pythagoreanTriplet)

colors = ["pink", "white", "blue", "black", "purple"]
color = [color.upper() for color in colors]
print(color)

heightInCMS = [('Carlos', 183), ('Lisa', 171), ('Lucia', 179), ('Wes', 165)]
heightInFeet = [(height[0], round(height[1] * 0.0328, 1)) for height in heightInCMS]
print(heightInFeet)

# Nested List Comprehensions[[]]
matrix = [[j * j+i for j in range(3)] for i in range(3)]
print(matrix)

# Set comprehensions {}
names = ['LUCIA', 'Wes', 'Addie', 'kendall', 'RapLh']
name = {name.capitalize() for name in names if len(name) > 1}
print(name)

#Dictionary Comprehensions {}
char_dict = {'A': 4, 'z': 2, 'D': 8, 'a': 5, 'Z' : 10}
letter_Count = {k.lower() :char_dict.get(k.lower(), 0) + char_dict.get(k.upper(),0) for k in char_dict.keys()}
print(letter_Count)