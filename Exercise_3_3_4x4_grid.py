"""
4x4 version grid
Think Python, 2nd Edition Ex3.3
"""

#two-by-two version of the grid.
def do_twice(f): 
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)
    
# four-by-four grid
def one_four_one(f, g, h):
    f()
    do_four(g)
    h()
    
# print '+' in each corners
def print_plus():
    print('+', end=' ')
    
# print the horizontal grid lines
def print_dash():
    print('-', end=' ')
    
#print the vertical grid lines
def print_bar():
    print('|', end=' ')
    
# print space in every grids
def print_space():
    print(' ', end=' ')
    
# print the end of the grid
def print_end():
    print()

# to create empty grid
def nothing():
    "do nothing"

#combining the four by four grids together

def print1beam():
    one_four_one(nothing, print_dash, print_plus)

def print1post():
    one_four_one(nothing, print_space, print_bar)

def print4beams():
    one_four_one(print_plus, print1beam, print_end)

def print4posts():
    one_four_one(print_bar, print1post, print_end)

def print_row():
    one_four_one(nothing, print4posts, print4beams)

def print_grid():
    # submitted version of this function should print
    # a four-by-four grid.  You can do that anyway you
    # want, but consider how you made do_four work.

    one_four_one(print4beams, print_row, nothing)
    
    # the following condition checks whether we are running as a
# script (like when you test the code), in which case run the
# test code, or being imported (say by the autograder), in
# which case don't.  Your main code should be "indented"
# within this conditional, just like the example code.

if __name__ == '__main__':

    # make this statement produce a 4x4 grid on the screen
    print_grid()



