import turtle

def init():
    """Initialize turtle"""
    turtle.up()
    turtle.title("Shapes")
    turtle.pensize(4)

def main():
    """Draw one set of embedded shapes"""
    init()
    draw_shape()
    turtle.rt(180)
    draw_shape()
    turtle.rt(180)

    turtle.color('black')
    turtle.done()

def draw_shape():
    square()
    circle()
    triangle()
    
def square():

    # draw square
    turtle.color('green')
    turtle.down()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.up()

def circle():

    # draw circle
    turtle.color('red')
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.down()
    turtle.circle(25)
    turtle.up()
    turtle.left(90)
    turtle.back(25)
    turtle.right(90)
    turtle.back(50)
def triangle():

    # draw triangle
    turtle.color('blue')
    turtle.down()
    turtle.forward(25)
    turtle.left(120)
    turtle.forward(25)
    turtle.left(120)
    turtle.forward(25)
    turtle.left(120)
    turtle.down()


main()