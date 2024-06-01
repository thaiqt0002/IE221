import turtle

win = turtle.Screen()
win.bgcolor('black')  # Set the background color to black

t = turtle.Turtle()
t.speed(1)
t.color("red", "pink")

def draw_heart(turtle):
    t.begin_fill()
    turtle.left(140)
    turtle.forward(200)
    turtle.circle(-100, 200)
    turtle.left(120)
    turtle.circle(-100, 200)
    turtle.forward(200)
    t.end_fill()
draw_heart(t)

turtle.done()