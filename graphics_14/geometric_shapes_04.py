import random
from turtle import Turtle, Screen
my_turtle = Turtle()
my_screen = Screen()
my_screen.setup(800,600)
my_turtle.penup()
my_turtle.goto(0,-150)
my_turtle.pendown()
colours_list = ['green', 'blue', 'red', 'pink', 'black', 'yellow']
my_turtle.shape('turtle')
my_turtle.color(random.choice(colours_list))

for i in range(3,11): # no of geometric shapes
    my_turtle.color(random.choice(colours_list))
    for j in range(i): # drawing each shape based on angle law
        angle = 360 / i
        my_turtle.forward(100)
        my_turtle.left(angle)









my_screen.exitonclick()