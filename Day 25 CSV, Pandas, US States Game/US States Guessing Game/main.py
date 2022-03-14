from turtle import *
import pandas
state_data = pandas.read_csv("50_states.csv")

screen = Screen()
screen.title("U.S. States guessing game")
screen.bgpic("blank_states_img.gif")

# image = "blank_states_img.gif"
# screen.addshape(image)
# turtle.shape(image)


    ### We actually dont need this code as we have coordinates from 50_states.csv ###

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()       # alt. to keep screen open after completion

         ###----------------------------------------------------------------------###


# correct_guesses = 0
states_guessed = []     # to keep track of all guesses guessed and avoid counting duplication of states
states_unguessed = []

# guesses_remaiming = True
# while guesses_remaining:
while len(states_guessed) < 50:
    answer_state = screen.textinput(title= f"{len(states_guessed)}/50 Guess state name",
                                    prompt= " Guess the state name").title()
    # answer_state = screen.textinput(title=f"{correct_guesses}/50 Guess state name",
    #                                 prompt=" Guess the state name").title()

    # print(answer_state)
    # print(state_data)

    if answer_state == "Exit":
        ## using normal code
        # for state in state_data['state']:
        #     if state not in states_guessed:
        #         states_unguessed.append(state)

        ## using list comprehension... 3 lines in 1 line
        states_unguessed = [state for state in state_data['state'] if state not in states_guessed]
        # print(states_unguessed)
        pandas.DataFrame(states_unguessed).to_csv("states_to_learn.csv")
        break

    # METHOD 1 (OWN) ##
    for state in state_data["state"]:

        if state == answer_state and answer_state not in states_guessed:
            states_guessed.append(answer_state)
            # correct_guesses += 1
            x_coor = state_data[state_data.state == state].x
            y_coor = state_data[state_data.state == state].y
            state_name = Turtle()
            state_name.hideturtle()
            state_name.penup()
            state_name.goto(int(x_coor),int(y_coor))
            state_name.write(state)



    # METHOD 2 (video) ##
    # all_states = state_data["state"].to_list()
    # # print(all_states)
    # if answer_state in all_states and answer_state not in states_guessed:
    #     states_guessed.append(answer_state)
    #     x_coor = state_data[state_data.state == answer_state].x
    #     y_coor = state_data[state_data.state == answer_state].y
    #     # print(x_coor, y_coor)
    #     # print(True)
    #     state_name = Turtle()
    #     state_name.hideturtle()
    #     state_name.penup()
    #     state_name.goto(int(x_coor), int(y_coor))
    #     state_name.write(answer_state)



    # if correct_guesses == 50:
    #     guesses_remaiming = False


screen.exitonclick()
