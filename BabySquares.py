import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")

laura = turtle.Turtle()
laura.color("hotpink")
laura.pensize(3)

def make_squares(turt,size,num):
    for j in range(num):
        turt.pendown()
        for i in range(4):
            turt.left(90)
            turt.forward(size)
        turt.penup()
        turt.forward(size*2)
        
make_squares(laura,20,5)