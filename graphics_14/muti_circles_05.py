from turtle import Turtle, Screen
import random

my_turtle = Turtle()
colours_list = ['green', 'red', 'blue', 'yellow', 'orange', 'black']
my_turtle.shape('turtle')

for i in range(10):
    my_turtle.color(random.choice(colours_list))
    my_turtle.circle(100)
    my_turtle.penup()
    my_turtle.left(10)
    my_turtle.pendown()

my_screen = Screen()
my_screen.exitonclick()