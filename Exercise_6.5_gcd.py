#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 16:05:10 2020

@author: meerarakesh09
"""


# Exercise 6.5  greatest common divisor (GCD) of a and b is the largest
# number that divides both of them with no remainder

def gcd(a, b):
    if b == 0:
        return a
    r = a % b # calculating GCD of remainder r
    return gcd(b, r)