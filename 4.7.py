import turtle
def make_window(colr, ttle):
    """
      Set up the window with the given background color and title.
      Returns the new window.
    """
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w


def make_turtle(colr, sz):
    """
      Set up a turtle with the given color and pensize.
      Returns the new turtle.
    """
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    return t
def make_square(turt):
    for i in range(4):
        turt.pendown()
        turt.forward(sz)
        turt.left(90)
    turt.penup()
    turt.forward(sz*2)
        
wn= make_window("lightgreen","squares")
ess= make_turtle("blue",5)
for i in range(5):
    make_square(ess,30)
