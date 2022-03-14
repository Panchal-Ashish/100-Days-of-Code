from turtle import *


timmy = Turtle()
my_screen = Screen()

def move_forward():     # as this function will be passed into another function, we should not assign input
    timmy.forward(10)

def move_backward():
    timmy.backward(10)

def move_left():
    timmy.left(10)

def move_right():
    timmy.right(10)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


my_screen.listen()

my_screen.onkey(key = 'w', fun = move_forward)
my_screen.onkey(key = 's', fun = move_backward)
my_screen.onkey(key = 'd', fun = move_right)
my_screen.onkey(key = 'a', fun = move_left)
my_screen.onkey(key = 'c', fun = clear)


my_screen.exitonclick()
