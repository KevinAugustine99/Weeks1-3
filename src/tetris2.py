#Kevin Augustine: Lab 02, tetris
import turtle
def board():
    #This function draws the tetris board
    #Pre: Turtle is facing east and pen up
    #Post: Turtle is facing east and pen up
    turtle.down()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.up()

def block():
    #This function draws one singular block.
    #Pre:Turtle is facing east and pen down in bottom left corner of the block
    #Post:Turtle is facing east and pen down in bottom left corner of the block
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    
def draw_B():
    #This function draws the block piece
    #Pre:Turtle is facing east and pen up in bottom left corner of the piece
    #Post:Turtle is facing east and pen up in bottom left corner of the piece
    turtle.down()
    turtle.fillcolor('red')
    turtle.begin_fill()
    block()
    turtle.forward(10)
    block()
    turtle.fd(10)
    turtle.lt(90)
    turtle.fd(20)
    turtle.lt(90)
    block()
    turtle.fd(10)
    block()
    turtle.end_fill()
    turtle.fd(10)
    turtle.lt(90)
    turtle.fd(20)
    turtle.lt(90)
    
    turtle.up()

def draw_I():
    #This function draws the tetris piece that is a line
    #Pre:Turtle is facing east and pen up in bottom left corner of the piece
    #Post:Turtle is facing east and pen up in bottom left corner of the piece
    turtle.down()
    turtle.fillcolor('green')
    turtle.begin_fill() 
    turtle.forward(10)
    turtle.lt(90)
    block()
    turtle.forward(10)
    block()
    turtle.forward(10)
    block()
    turtle.forward(10)
    block()
    turtle.end_fill()
    turtle.bk(30)
    turtle.rt(90)
    turtle.bk(10)
    
    turtle.up()

def draw_S():
    #This function draws the s block piece
    #Pre:Turtle is facing east and pen up in bottom left corner of the piece
    #Post:Turtle is facing east and pen up in bottom left corner of the piece
    turtle.down()
    turtle.fillcolor('yellow')
    turtle.begin_fill()
    block()
    turtle.forward(10)
    block()
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    block()
    turtle.right(90)
    block()
    turtle.end_fill()
    turtle.up()
    turtle.forward(10)
    turtle.bk(30)
    turtle.rt(90)
    turtle.fd(10)
    turtle.lt(90)

def draw_Z():
    #This function draws the z block piece
    #Pre:Turtle is facing east and pen up in bottom left corner of the piece
    #Post:Turtle is facing east and pen up in bottom left corner of the piece
    turtle.fillcolor('purple')
    turtle.begin_fill()
    turtle.fd(10)
    turtle.begin_fill()
    turtle.down()
    block()
    turtle.fd(10)
    block()
    turtle.lt(90)
    turtle.fd(20)
    turtle.lt(90)
    block()
    turtle.fd(10)
    block()
    turtle.end_fill()
    turtle.up()
    turtle.rt(90)
    turtle.bk(20)
    turtle.rt(90)
    turtle.bk(10)


def draw_T():
    #This function draws the t block piece
    #Pre:Turtle is facing east and pen up in bottom left corner of the piece
    #Post:Turtle is facing east and pen up in bottom left corner of the piece
    turtle.down()
    turtle.fillcolor('blue')
    turtle.begin_fill()
    block()
    turtle.forward(10)
    block()
    turtle.forward(10)
    block()
    turtle.left(90)
    turtle.forward(10)
    block()
    turtle.end_fill()
    turtle.up()
    turtle.back(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.bk(30)


def draw_J():
    #This function draws the J block piece
    #Pre:Turtle is facing east and pen up in bottom left corner of the piece
    #Post:Turtle is facing east and pen up in bottom left corner of the piece
    turtle.down()
    turtle.fillcolor('brown')
    turtle.begin_fill()
    block()
    turtle.forward(10)
    block()
    turtle.forward(10)
    turtle.lt(90)
    turtle.forward(10)
    block()
    turtle.forward(10)
    block()
    turtle.end_fill()
    turtle.up()
    turtle.back(20)
    turtle.right(90)
    turtle.bk(20)
    

def draw_L():
    #This function draws the L block
    #Pre:Turtle is facing east and pen up in bottom left corner of the piece
    #Post:Turtle is facing east and pen up in bottom left corner of the piece
    turtle.down()
    turtle.fillcolor('orange')
    turtle.begin_fill()
    block()
    turtle.forward(10)
    block()
    turtle.lt(90)
    turtle.forward(10)
    block()
    turtle.forward(10)
    block()
    turtle.end_fill()
    turtle.up()
    turtle.back(20)
    turtle.right(90)
    turtle.forward(-10)
    

def place_object(X,Y,D,O):
    #This function moves the turtle to the correct position, draws the object, and then goes back.
    #Pre:Turtle is facing east and pen up in bottom left corner of the board
    #Post:Turtle is facing east and pen up in bottom left corner of the board
    
    turtle.fd(X)
    turtle.lt(90)
    turtle.fd(Y)
    turtle.rt(90)
    draw_object(D,O)
    turtle.fd(-X)
    turtle.lt(90)
    turtle.fd(-Y)
    turtle.rt(90)

def draw_object(D,O):
    #This function draws one of the 7 pieces in the right rotation
    if O == "B":
        draw_B()
    elif O == "I":
        if D == 0 or D == 180:
            draw_I()
        elif D == 90 or D == 270:
            turtle.rt(90)
            turtle.bk(10)
            draw_I()
            turtle.fd(10)
            turtle.left(90)
    elif O == "Z":
        if D == 0 or D == 180:
            turtle.bk(10)
            draw_Z()
            turtle.fd(10)
        elif D == 90 or D == 270:
            turtle.forward(20)
            turtle.lt(90)
            draw_Z()
            turtle.rt(90)
            turtle.bk(20)
    elif O == "S":
        if D == 0 or D == 180:
            draw_S()
        elif D == 90 or D == 270:
            turtle.forward(10)
            turtle.lt(90)
            draw_S()
            turtle.rt(90)
            turtle.bk(10)
    elif O == "J":
        if D == 0:
            draw_J()
        elif D == 90:
            turtle.fd(10)
            turtle.lt(90)
            draw_J()
            turtle.rt(90)
            turtle.bk(10)
        elif D == 180:
            turtle.fd(20)
            turtle.lt(90)
            turtle.fd(30)
            turtle.lt(90)
            draw_J()
            turtle.lt(-90)
            turtle.fd(-30)
            turtle.lt(-90)
            turtle.fd(-20)
        elif D == 270:
            turtle.rt(90)
            turtle.bk(20)
            draw_J()
            turtle.fd(20)
            turtle.lt(90)
    elif O == "L":
        if D == 0:
            draw_L()
        elif D == 90:
            turtle.fd(30)
            turtle.lt(90)
            draw_L()
            turtle.rt(90)
            turtle.bk(30)
        elif D == 180:
            turtle.fd(10)
            turtle.lt(90)
            turtle.fd(30)
            turtle.lt(90)
            draw_L()
            turtle.lt(-90)
            turtle.fd(-30)
            turtle.lt(-90)
            turtle.fd(-10)
        elif D == 270:
            turtle.rt(90)
            turtle.bk(20)
            draw_L()
            turtle.fd(20)
            turtle.lt(90)
    elif O == "T":
        if D == 0:
            draw_T()
        elif D == 90:
            turtle.forward(10)
            turtle.lt(90)
            draw_T()
            turtle.lt(-90)
            turtle.forward(-10)
        elif D == 180:
            turtle.fd(20)
            turtle.lt(90)
            turtle.fd(20)
            turtle.lt(90)
            draw_T()
            turtle.lt(-90)
            turtle.fd(-20)
            turtle.lt(-90)
            turtle.fd(-20)
        elif D == 270:
            turtle.rt(90)
            turtle.bk(30)
            draw_T()
            turtle.fd(30)
            turtle.left(90)

def ask_user():
    #This function asks the user which piece, rotation, and position they want the block placed
    O = input("Enter a letter {BILJZST} to choose the shape to place:")
    D = int(input("Enter 0, 90, 180, 270 for the rotation:"))
    print("Row and column is where to place the lower left block of a shape.")
    Y = int(input("Enter a row number (0 to 19) for lower left space:"))*10
    X = int(input("Enter a column number (0 to 9) for lower left space:"))*10
    print("close the canvas window to quit")
    place_object(X,Y,D,O)

def main():

    turtle.speed(0)
    turtle.up()
    board()
    place_object(0,0,0,"L")
    place_object(20,0,270,"J")
    place_object(30,10,0,"B")
    place_object(50,0,90,"Z")
    place_object(80,0,90,"T")
    place_object(60,30,90,"I")
    place_object(10,30,0,"Z")
    place_object(30,30,0,"S")


    ask_user()
    
    turtle.done()
    

if __name__ == "__main__":
    main()
