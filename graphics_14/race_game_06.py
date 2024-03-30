import random
import time
from turtle import Turtle, Screen


def draw_turtle(turtle_name, turtle_color, y_pos):
    turtle_name = Turtle()
    turtle_name.shape('turtle')
    turtle_name.shapesize(1.5)
    turtle_name.color(turtle_color)
    turtle_name.penup()
    turtle_name.goto(-300, y_pos)
    turtle_name.pendown()
    return turtle_name


def move_func():
    if not end_game:
        green_turtle.forward(10)


def black_white_line(x_cor, y_cor, square_colour, angle):
    my_turtle.penup()
    my_turtle.goto(x_cor, y_cor)
    my_turtle.pendown()
    my_turtle.shape('square')
    my_turtle.shapesize(1)
    my_turtle.color(square_colour)
    my_turtle.stamp()
    my_turtle.right(angle)
    for i in range(9):
        my_turtle.penup()
        my_turtle.forward(40)
        my_turtle.stamp()
        my_turtle.pendown()


# main program

my_turtle = Turtle()

# Screen Setup
my_screen = Screen()
my_screen.setup(800, 500)
my_screen.title('Race Game')
my_screen.bgcolor('green')

# Heading
my_turtle.penup()
my_turtle.goto(-100, 205)
my_turtle.color('white')
my_turtle.write('Turtle Race', font=('ariel', 20, 'bold'))

# Floor
my_turtle.goto(-350, 200)
my_turtle.pendown()
my_turtle.color('chocolate')
my_turtle.begin_fill()
for i in range(2):
    my_turtle.forward(700)
    my_turtle.right(90)
    my_turtle.forward(400)
    my_turtle.right(90)
my_turtle.end_fill()

# Black_White Race Line
black_white_line(250, 190, 'black', 90)  # Black-01
black_white_line(250, 170, 'white', 0)  # White-01
black_white_line(270, 190, 'white', 0)  # White-02
black_white_line(270, 170, 'black', 0)  # Black-02

# Draw Turtles
blue_turtle = draw_turtle('blue_turtle', 'blue', 150)
pink_turtle = draw_turtle('pink_turtle', 'pink', 50)
yellow_turtle = draw_turtle('yellow_turtle', 'yellow', -50)
green_turtle = draw_turtle('green_turtle', 'green', -150)

# Pause_Race
end_game = False
time.sleep(3)

# Moving green turtle by manual control
my_screen.listen()
my_screen.onkey(move_func, "Right")

# Moving_Turtles

while True:
    blue_turtle.forward(random.randint(1, 5))
    pink_turtle.forward(random.randint(1, 5))
    yellow_turtle.forward(random.randint(1, 5))
    # green_turtle.forward(random.randint(1,5))

    if blue_turtle.xcor() > 230:
        winner = blue_turtle
        break
    elif pink_turtle.xcor() > 230:
        winner = pink_turtle
        break
    elif yellow_turtle.xcor() > 230:
        winner = yellow_turtle
        break
    elif green_turtle.xcor() > 230:
        winner = green_turtle
        break

# celebrate winner
end_game = Turtle
winner.shapesize(2.5)
for j in range(1000):
    winner.right(5)


my_screen.exitonclick()
