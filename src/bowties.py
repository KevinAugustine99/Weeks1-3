"""
File : bowties.py
Assignment : Lab #3
Language : python3
Author : Kevin Augustine < kea4437@rit.edu >
Purpose : Draws bowties recursively
"""

import turtle


def draw_one_bowtie(size: int):
    """draw_one_bowtie draws one bowtie.
        size (int): The length of one side of the bowties
        Pre: 
        Turtle is up and facing to the right of the bowtie
        Post: 
        Turtle is up, facing the right of the bowtie, and the bowtie has been drawn
    """

    turtle.pencolor('blue')
    turtle.down()
    turtle.lt(30)
    turtle.fd(size)
    turtle.rt(120)
    turtle.fd(size)
    turtle.rt(120)
    turtle.fd(size * 2)
    turtle.lt(120)
    turtle.fd(size)
    turtle.lt(120)
    turtle.fd(size)
    turtle.rt(30)
    turtle.up()
    turtle.rt(90)
    turtle.fd(size / 4)
    turtle.lt(90)
    turtle.fillcolor('red')
    turtle.down()
    turtle.begin_fill()
    turtle.circle(size / 4)
    turtle.end_fill()
    turtle.up()
    turtle.lt(90)
    turtle.fd(size / 4)
    turtle.rt(90)


def draw_bowties(depth, size):
    """draw_bowties draws the bowties recursively.
       size (int): The length of one side of the center bowtie = 90
       depth (int): The depth of the recursion.
       Pre: 
        Turtle is up, in the center, and facing east
       Post: 
        Turtle is up, in the center, facing east, and all of the bowties have been drawn
    """

    if depth == 0:
        pass
    if depth == 1:
        draw_one_bowtie(size)
    else:
        draw_one_bowtie(size)
        turtle.lt(30)
        turtle.fd(size * 2)
        draw_bowties(depth - 1, size / 3)
        turtle.bk(size * 2)
        turtle.lt(120)
        turtle.fd(size * 2)
        turtle.rt(180)
        draw_bowties(depth - 1, size / 3)
        turtle.lt(180)
        turtle.bk(size * 2)
        turtle.rt(150)
        turtle.rt(180)
        turtle.lt(30)
        turtle.fd(size * 2)
        draw_bowties(depth - 1, size / 3)
        turtle.bk(size * 2)
        turtle.lt(120)
        turtle.fd(size * 2)
        turtle.rt(180)
        draw_bowties(depth - 1, size / 3)
        turtle.lt(180)
        turtle.bk(size * 2)
        turtle.rt(150)
        turtle.lt(180)


def main():
    depth = int(input("What depth would you like? Please choose a number greater than 0:"))
    turtle.speed(0)
    draw_bowties(depth, 90)

    turtle.done()


if __name__ == "__main__":
    main()
