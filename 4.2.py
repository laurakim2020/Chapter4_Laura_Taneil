import turtle

def make_squares(turt,size,num):s
    
    #we're using two variables for size,
    #origSize stayes the same in order to keep the spacing the same
    #size increases by origSize with each repitition

    origSize = size
    for j in range(num):
        turt.pendown()
        
        for i in range(4):
            turt.forward(size)
            turt.left(90)
        turt.penup()
        turt.backward(origSize/2)
        turt.right(90)
        turt.forward(origSize/2)
        turt.left(90)
        size = size + origSize
        

wn = turtle.Screen()
wn.bgcolor("green")

huh=turtle.Turtle()
huh.color("blue")
huh.pensize(3)
huh.speed(10)


make_squares(huh,20,5)