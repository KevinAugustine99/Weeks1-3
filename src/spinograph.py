
from math import *
import turtle

R = 100
r = 4

def getX(t,p):
    return (R - r) * cos(t) - (r + p) * cos((R -r) / r * t)

def getY(t,p):
    return (R - r) * sin(t) - (r + p) * sin((R -r) / r*t)

def draw(p):
    t = 2*pi
    while (t >= 0):
        turtle.pendown()
        turtle.goto(getX(t,p),getY(t,p))
        t -= 0.01
        


def main():
    #  p = int(input("What is p?"))
    p = 50
    turtle.speed(0)
    draw(p)
    turtle.done()



if __name__ == "__main__":
    main()

