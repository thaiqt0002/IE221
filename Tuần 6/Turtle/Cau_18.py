import turtle

t = turtle.Turtle()
t.speed(2)
t.color('black')

# Hide the turtle
t.hideturtle()

# Move the turtle to a suitable position
t.penup()
t.goto(-150, -50)
t.pendown()

# Write the text
t.write("Cool python codes", align="left", font=("Freestyle Script", 50))

turtle.done()