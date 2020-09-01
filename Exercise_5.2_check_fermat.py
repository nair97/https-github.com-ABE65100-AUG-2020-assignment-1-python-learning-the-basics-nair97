#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 15:45:46 2020

@author: meerarakesh09
Write function to check fermat theorem that:
a**n + b**n = c**n works or not
"""
  # to check if fermat theorem formula works or not
def check_fermat(a,b,c,n):  
    if (n>2) and (a**n + b**n == c**n):
        print("Holy smoke!Fermat was wrong!")
    else:
        print("No! that doesnt work")
 # to input values for the parameters and return check_fermat 
def check_number():
    a = int(input("Choose a number for a: "))
    b = int(input("Choose a number for b: "))
    c = int(input("Choose a number for c: "))
    n = int(input("Choose a number for n: "))
    return check_fermat(a,b,c,n)

check_number()