from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.shape('turtle')
my_turtle.color('red')
my_screen = Screen()
my_screen.setup(800, 600)
my_turtle.penup()
my_turtle.goto(-400, 0)

my_turtle.pendown()
for i in range(50):
    my_turtle.forward(5)
    my_turtle.penup()
    my_turtle.forward(5)
    my_turtle.pendown()

my_screen.exitonclick()
