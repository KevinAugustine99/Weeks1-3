#Kevin Augustine
import turtle
def draw_triangle():
	""" draw_triangle causes the turtle to draw the triangle and lines up the turtle to draw the next triangle"""

	turtle.lt(60)
	turtle.fd(100)
	turtle.rt(120)
	turtle.fd(100)
	turtle.rt(120)
	turtle.fd(100)
	turtle.bk(100)
	turtle.lt(108)

	
def main():

	"""main causes the program to change the turtle's speed to 3 and runs the draw_triangle function five times"""
	turtle.speed(3)
	draw_triangle()
	draw_triangle()
	draw_triangle()
	draw_triangle()
	draw_triangle()
	turtle.done()

	
main()
