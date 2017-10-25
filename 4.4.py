import turtle

def make_shape(turt,size,ang):
    for a in range(6):
        turt.right(ang)
        
        for i in range(4):
            turt.forward(size)
            turt.left(90)
        
        for b in range(4):
            turt.backward(size)
            turt.left(90)
        
        for c in range(4):
            turt.backward(size)
            turt.right(90)
        
        for d in range(4):
            turt.forward(size)
            turt.right(90)
            

wn = turtle.Screen()
wow=turtle.Turtle()
wn.bgcolor("green")
wow.speed(0)
wow.pensize(3)
wow.color("blue")

make_shape(wow,100,18)

wn.mainloop