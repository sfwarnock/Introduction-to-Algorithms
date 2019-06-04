# -*- coding: utf-8 -*-
"""
Created on Mon May 20 06:28:39 2019

@author: Scott Warnock
"""

"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

    The number of elements initialized in nums1 and nums2 are m and n respectively.
    You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

"""

def mergeSort(a1, a2):  
    #sort the array which will be merged
    print(a1)
    for index in range(len(a1)):
    
        subArray1 = a1[index]
        position = index
        print('subArray1 = ',subArray1, 'position = ', position, )

        while position > 0 and a1[position - 1] > subArray1:
            print('a1[position-1]', a1[position-1], '>', subArray1, 'subArray1')
            a1[position] = a1[position - 1]
            position = position - 1
    
        a1[position] = subArray1
        print(a1[position], 'a1[position], loop complete')
        print(a1)
        print(' ')

    #merge a2 into a1
    # for digit in a2:
        # if digit > a1[digit]
            # insert digit into a1[digit + 1]
        # else
            # a1[digit] + 1
            
a1 = [9, 1, 3, 7, 5]
a2 = [4, 2, 10, 6, 8]

mergeSort(a1, a2)