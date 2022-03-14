from turtle import *
import time

screen = Screen()
screen.title("Snake game")
screen.setup(width = 600,height = 600)
screen.bgcolor("black")
screen.tracer(0)


### CREATING THE SNAKE BODY ###

# # Method 1
# new_segment_1 = Turtle("square")
# new_segment_1.color("white")
#
# new_segment_2 = Turtle("square")
# new_segment_2.color("white")
# new_segment_2.goto(-20, 0)
#
# new_segment_3 = Turtle("square")
# new_segment_3.color("white")
# new_segment_3.goto(-40, 0)


# Method 2
segments = []
starting_positions = [(0,0),(-20,0),(-40,0)]
for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


### MAKING THE SNAKE BODY MOVE ###

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    ## making it move straight (only).... if turned, only first segment turns and rest continues straight
    ## tail does not follow the head
    # for seg in segments:
    #     seg.forward(20)


    for seg in range((len(segments) - 1), 0,-1):
        ## making a particular segment to goto the position of the previous segment... like 3 to 2, 2 to 1, 1 to new
        ## making the tail to follow the head
        new_x = segments[seg - 1].xcor()
        new_y = segments[seg - 1].ycor()
        segments[seg].goto(new_x,new_y)
    segments[0].forward(20)





























screen.exitonclick()