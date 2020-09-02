# -*- coding: utf-8 -*-
"""
Spyder Editor

To draw 3 set of flowers using turtle module
by Meera - 09-01-2020
"""

import math
import turtle
#math function provides all mathematical functions
#turtle module creates images
# import the tkinter graphics library tools.  Note that is was called Tkinter for
# Python 2
from tkinter import *

def polyline(obj, length, sides, angle):
    for i in range(sides):
        obj.fd(length)
        obj.lt(angle)
    #Generalizing polyline to take angle and length to draw arc for petals

def arc(t, radius, angle):
    arc_length = 2 * math.pi * radius * angle / 360
    sides = int(arc_length / 3) + 1
    step_length = arc_length / sides
    step_angle = angle / sides
    #rewriting arc to use polyline
    #calculating the arc length and angle for petal formation

    polyline(obj = t, length = step_length, sides = sides, angle = step_angle)

def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180.0-angle)
        #creating the petal using arc

def flower(t, n, r, angle):
    """
    t: turtle
    n: number of petals in the flower
    r: radius of the arcs
    angle: angle that subtends the arc
    """
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0/n)
        #creating flower using petal

def move_turtle(t, length):
    t.pu()
    t.fd(length)
    t.pd()
    #moving pen up and down using turtle to draw the flower

bob = turtle.Turtle()
# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':

    # Indent your control code here so that it does not
    # run if functions are imported by another program.
# draw the first flower
  move_turtle(bob, -200)
  flower(bob, 7, 60.0, 60.0)
 # move to next location, draw second flower
  move_turtle(bob, 200)
  flower(bob, 10, 50.0, 70.0)
# move to next location, draw third flower
  move_turtle(bob, 200)
  flower(bob, 20, 120.0, 20.0)

bob.hideturtle()

ts = turtle.getscreen() # grab the drawing screen for later use
ts.getcanvas().postscript(file="flower.eps") # extract the image and save as a postscript file
turtle.bye() # close the drawing screen and end the turtle session

