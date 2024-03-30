from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.shape('turtle')

my_turtle.color('blue')

my_turtle.fillcolor('green')
my_turtle.begin_fill()
for i in range(4):
    my_turtle.forward(100)  # distance
    my_turtle.left(90)    # angle
my_turtle.end_fill()

my_turtle.penup()    # no draw
my_turtle.goto(-200, 200)   # coordinates x,y
my_turtle.pendown()  # draw again
my_turtle.forward(200)

# stamping
my_turtle.shape('square')
my_turtle.stamp()
my_turtle.forward(100)
my_turtle.stamp()
my_turtle.right(60)
my_turtle.forward(100)
my_turtle.dot()
my_turtle.forward(100)
my_turtle.shape('turtle')

my_turtle.fillcolor('red')
my_turtle.begin_fill()
my_turtle.circle(40)
my_turtle.end_fill()




my_screen = Screen()
my_screen.exitonclick()
