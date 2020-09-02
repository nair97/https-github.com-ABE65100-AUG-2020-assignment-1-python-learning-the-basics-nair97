#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 16:05:10 2020

@author: meerarakesh09
"""
# import math functions
import math

#functions to calculate newton's square root
def mysqrt(a):
    x = a/2
    epsilon = 0.0000001
    while True:
        print(x)
        y = (x + a/x)/2
        if abs(y-x) < epsilon:
           break
        x = y
    return x

#to test and print table using loop
def test_square_root(num=10):

    d = square_root(a) - mysqrt(a)
    return d
    print("a        mysqrt(a)        math.sqrt(a)        diff")
    print("---     ----------       -------------       ------")
    for a in range(1, num):
        print (a,"  ",mysqrt(a),"  ",math.sqrt(a),"  ",abs (mysqrt(a) - math.sqrt(a)),"  ")
   
test_square_root()
