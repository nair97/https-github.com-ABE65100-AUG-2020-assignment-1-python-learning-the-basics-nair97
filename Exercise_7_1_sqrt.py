#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 16:05:10 2020

@author: meerarakesh09
"""

# import math module
import math

#functions and conditional loops to calculate newton's square root method
def mysqrt(a):
    x = a/2
    while True:
         y = (x + a/x)/2
         if y == x:
             return y
             break
         x = y

#to test and print table using loop format
def test_square_root(num_a):
  #construct spacing between columns
    sp1 = "  "
    sp2 = "  " * 3
    sp3 = " "
#to list table headers and columns
    print("a", sp1, "mysqrt(a)", sp2, "math.sqrt(a)", sp3, "diff")
    print("---", sp1, "----------", sp2, "-------------", sp3, "------") # to fill space and underline the headers
#loop to calculate the square root method and print according to the table format in columns
    for a in num_a:
        c1 = float(a)
        c2 = mysqrt(a)
        c3 = math.sqrt(a)
        c4 = abs(mysqrt(a) - math.sqrt(a))
        print(c1, "{:<10f}".format(c2), "{:<12f}".format(c3), c4)
        
# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.
if __name__ == '__main__':
        
         test_square_root(range(1,10))
         
         
    
    
    