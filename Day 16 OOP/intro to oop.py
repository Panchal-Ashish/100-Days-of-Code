import turtle
from turtle import Turtle,Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.forward(45)
timmy.color("green4")
timmy.right(45)
timmy.backward(45)
timmy.setpos(45,80)
print(timmy.pos())
print(turtle.heading())
timmy.left(90)


my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
