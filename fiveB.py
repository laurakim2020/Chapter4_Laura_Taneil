import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")

laura = turtle.Turtle()
laura.color("blue")

def draw_spiral(turt,angle):
    length = 1
    for i in range(84):
        turt.forward(length)
        turt.right(angle)
        length = length + 2
        
laura.home()
laura.penup()
laura.forward(90)
laura.pendown()

draw_spiral(laura,89)