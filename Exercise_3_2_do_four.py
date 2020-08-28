#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 15:41:41 2020

@author: meerarakesh09
"""

def do_twice(func, arg):
    
    func(arg)
    func(arg)


def print_twice(arg):
    
    print(arg)
    print(arg)


def do_four(func, arg):
   
    do_twice(func, arg)
    do_twice(func, arg)


do_twice(print, 'spam')
print('spam')

do_four(print, 'spam')