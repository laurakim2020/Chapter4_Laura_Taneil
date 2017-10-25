#Extend your program above
#turn right by 144, put the pen down, and draw the next star. You’ll get something like this:
import turtle
greg=turtle.Turtle()
def draw_star():
    greg.right(216)
    for i in range(4):
        greg.speed(0)
        greg.forward(100)
        greg.left(216)
    greg.forward(100)
draw_star()