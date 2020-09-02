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
   
    if b == 0:
          return a
    else:
          return gcd(b, a%b) #calculate gcd value
      
#entering values for computing GCD
num_a = int(input(" enter the value for a: "))
num_b = int(input(" enter the valur for b: "))

# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':

       print("The GCD is: ",num_a, num_b)
       
gcd(num_a, num_b)

       
       
    



      







 

          