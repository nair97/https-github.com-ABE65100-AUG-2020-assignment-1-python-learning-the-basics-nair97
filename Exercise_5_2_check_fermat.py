#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 15:45:46 2020

@author: meerarakesh09
Write function to check fermat theorem that:
a**n + b**n = c**n works or not
"""
  # to check if fermat theorem formula works or not
def check_fermat(a, b, c, n):  
#Fermat's Last Theorem Function takes 4 inputs and check whether Fermat's Last Theorem is valid
#a,b,c : Positive integers n: Any value greater than n

    if n > 2 and (a**n + b**n == c**n):
        
          print("Holy smokes, Fermat was wrong!")
    else:
          print("No, that doesn’t work.")
       
 # to input values for the parameters and return check_fermat 
def check_numbers():
 
    a = int(input("Choose a number for a: "))
    b = int(input("Choose a number for b: "))
    c = int(input("Choose a number for c: "))
    n = int(input("Choose a number for n: "))
   
    return check_fermat(a, b, c, n)

if __name__ == '__main__':

   check_numbers()