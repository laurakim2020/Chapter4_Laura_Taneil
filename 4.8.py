import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
s = turtle.Turtle()
s.color("blue")
s.pensize(3)
def draw_poly(turt,num,size):
    for i in range(num):
        turt.forward(size)
        turt.left(360/num)
        turt.speed(0)


def draw_equitriangle(t, sz):
    for i in range(3):
        t.forward(sz)
        t.left(120)
        t.speed(0)
        
draw_equitriangle(s, 100)
        