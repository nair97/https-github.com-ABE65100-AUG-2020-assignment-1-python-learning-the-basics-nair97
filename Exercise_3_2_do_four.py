#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 15:41:41 2020

@author: meerarakesh09
"""

# to run the function 2 times
def do_twice(func, arg):
    """Runs a function twice.
    func: function object
    arg: argument passed to the function
    """
    # input function to run twice
    func(arg)
    func(arg)
    
# to print the argument 2 times
def print_twice(arg):
    """Prints the argument twice.
    arg: anything printable
    """
    # print argument (arg) twice
    print(arg)
    print(arg)
    
# to run the funtion 4 times
def do_four(func, arg):
    """Runs a function four times.
    func: function object
    arg: argument passed to the function
    """
    
    # input the function do_twice 2 times to run 4 times
    do_twice(func, arg)
    do_twice(func, arg)

# the following condition checks whether we are running as a
# script (like when you test the code), in which case run the
# test code, or being imported (say by the autograder), in
# which case don't.  Your main code should be "indented"
# within this conditional, just like the example code.

if __name__ == '__main__':


    # start by making this work (and adding your own comments)
    do_twice(print, 'spam')

    # then make this statement work (do not forget to remove the #)
    do_twice(print_twice, 'spam')

    # finally, make this statement work
    do_four(print_twice, 'spam')