import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")

laura = turtle.Turtle()
laura.color("hotpink")
laura.pensize(3)

def draw_poly(turt,num,size):
    for i in range(num):
        turt.forward(size)
        turt.left(360/num)
        
draw_poly(laura,8,50) 
    
