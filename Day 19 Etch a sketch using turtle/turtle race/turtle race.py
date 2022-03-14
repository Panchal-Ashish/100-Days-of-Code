from turtle import *
import random

race_on = False

my_screen = Screen()
my_screen.setup(width=500, height=400)

user_bet = my_screen.textinput(title="Make your bet",
                               prompt="Which turtle will win the race? Enter a color "
                                      "(red, green, blue, orange, black, purple): ").lower()
## textinput method returns the string of text... so it is stored in another variable for future refernce

colors = ["red", "green", "blue", 'orange', "black", "purple"]
y_pos = [-90, -50, -10, 30, 70, 110]
all_turtles = []

if user_bet in colors:
    race_on = True
    for turtle_index in range(len(colors)):
        new_turtle = Turtle(shape='turtle')  ## shape can also be specified separately... turtle class has optional parameter input of shape, so just using that
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x=-235, y=y_pos[turtle_index])
        new_turtle.speed(0.2)
        all_turtles.append(new_turtle)
else:
    print("incorrect input")


while race_on:
    for turtle in all_turtles:
        turtle.forward(random.randint(0,10))
        if turtle.xcor() >= 225:
            race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You Won!!! {winner} turtle won the race")
            else:
                print(f"You lost!!! {winner} turtle won the race")

my_screen.exitonclick()
