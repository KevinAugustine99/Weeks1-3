"""
File : circles.py
Assignment : Homework #3
Language : python3
Author : Kevin Augustine < kea4437@rit.edu >
Purpose : Draws circles recursively.
"""

import turtle

def move_initial():
    """This function moves the turtle to its starting position.
       Pre: 
        Turtle is down and facing east.
       Post: 
        Turtle is up, facing east, and 150 units closer to the bottom.

    """    
    turtle.up()
    turtle.lt(90)
    turtle.bk(150)
    turtle.rt(90)
def draw_circles(N,radius):
    """draw_circles draws the circles recursively.
       N (int): The depth of the recursion
       Radius(int): The radius of the circle
       Pre: 
        Turtle is up and facing east.
        N>0
        Radius=200
       Post: 
        Turtle is up, facing east, and circle(s) have been drawn
    """    
    
    if N == 1:
        turtle.down()
        turtle.circle( radius )
        turtle.up()
    else :
        turtle.down()
        turtle.circle( radius )
        turtle.up()
        turtle.bk(radius)
        turtle.rt(90)
        turtle.bk(radius)
        turtle.lt(90)
        turtle.down()
        draw_circles(N-1, radius/2)
        turtle.up()
        turtle.fd(2*radius)
        turtle.down()
        draw_circles(N-1,radius/2)
        turtle.up()
        turtle.rt(90)
        turtle.fd(radius)
        turtle.lt(90)
        turtle.bk(radius)     

def main():
    N = int(input("What depth of the circle recursion would you like? Please choose a number greater than 0:"))
    turtle.speed(0)
    move_initial()
    draw_circles(N,200)
    turtle.done()

if __name__ == "__main__":
    main()
