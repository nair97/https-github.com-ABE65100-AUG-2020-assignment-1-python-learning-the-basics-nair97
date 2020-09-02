#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 16:05:10 2020

@author: meerarakesh09
"""
#The greatest common divisor (GCD) of a and b is the largest number that 
#divides both of them with no remainder.

def gcd(a, b):
   # a, b: positive integers
    #returns: a positive integer, the greatest common divisor of a & b.
    # Base case is when b = 0
    r = a % b
    if b == 0:
        return a
        return gcd(b, r) #calculate gcd value