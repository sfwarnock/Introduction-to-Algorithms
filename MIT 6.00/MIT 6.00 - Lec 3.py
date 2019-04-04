# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 06:24:01 2019

@author: Scott Warnock
"""

x = 25
ans = 0

if x >= 0:
    while ans*ans < x:
        ans = ans + 1
        #print ('ans = ', ans)
    if ans * ans != x:
        print('x is not a perfect square')
    else:
        print(ans)
else: print ('x is a negative number')

y = 10
for i in range(1, y):
    if y % i == 0:
        print('Divisor', i)
        
foo = (1, 2, 3, 4, 5)   #Tuple
bar = [1, 2, 3, 4, 5]   #List
print(foo[1], bar[1])

z = 100
div = ()
for i in range(1,z):
    if z % i == 0:
        div = div + (i,)
print(div)