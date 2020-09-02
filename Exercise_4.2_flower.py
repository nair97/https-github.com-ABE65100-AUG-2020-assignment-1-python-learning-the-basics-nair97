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

move_turtle(bob, -200)
flower(bob, 7, 60.0, 60.0)

move_turtle(bob, 200)
flower(bob, 10, 50.0, 70.0)

move_turtle(bob, 200)
flower(bob, 20, 120.0, 20.0)

bob.hideturtle()
turtle.mainloop()


# After drawing the three flowers: DO NOT include the command turtle.done()
# or turtle.mainloop() - these commands just freeze the open window.  Instead
# add the following sequence of commands.
ts = turtle.getscreen() # grab the drawing screen for later use
ts.getcanvas().postscript(file="flower.eps") # extract the image and save as a postscript file
turtle.bye() # close the drawing screen and end the turtle session
