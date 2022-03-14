from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    # to_learn = data.to_dict(orient= "index")    ## please go through pandas orient documentation, important
    # print(to_learn[0]["French"])
    to_learn = data.to_dict(orient= "records")
    # print(to_learn)

## both record and index methods in orient works in this case... have a look thru documnetation
## https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html#pandas.DataFrame.to_dict


current_card = {}
## ------------------------------SHOW ANSWER -----------------------##


def flip():
    canvas.itemconfig(background_image, image= back_image)
    canvas.itemconfig(title_text, text="English", fill = "red")
    canvas.itemconfig(word_text, text=current_card["English"], fill = "red")
    # window.after(1000, func= new_word)


## ------------------------------- NEW WORD --------------------------##

def new_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(background_image, image= front_image)
    canvas.itemconfig(title_text, text= "French", fill = "black")
    canvas.itemconfig(word_text, text= current_card["French"], fill = "black")
    flip_timer = window.after(3000, func= flip)


def is_known():
    to_learn.remove(current_card)
    updated_data = pandas.DataFrame(to_learn)
    updated_data.to_csv("data/word_to_learn.csv", index= 0)
    new_word()


## ------------------------------- UI setup ---------------------------##
window = Tk()
window.title("Flashcard project")
window.config(padx= 50, pady= 50, bg= BACKGROUND_COLOR)

flip_timer = window.after(3000, func= flip)


canvas = Canvas(width= 600, height= 400, bg= BACKGROUND_COLOR, highlightthickness= 0)
front_image = PhotoImage(file= "./images/card_front.png")
back_image= PhotoImage(file= "./images/card_back.png")

background_image = canvas.create_image(300,200,image= front_image)
title_text = canvas.create_text(300,120,text= "French", font= ("arial", 32,"italic"))   ## X and Y coordinates are w.r.t. to canvas
word_text = canvas.create_text(300,280,text= "word", font= ("arial", 32,"bold"))
canvas.grid(row= 0,column= 0, columnspan= 2)


## BUTTONS
tick_image = PhotoImage(file= "./images/right.png")
right_button = Button(image= tick_image, highlightthickness= 0, command= is_known)
right_button.grid(row= 1, column= 0)

cross_image = PhotoImage(file= "C:/Users/Manoj/PycharmProjects/Udemy 100 days of code/Day 31 Flash card project/images/wrong.png")
wrong_button = Button(image= cross_image, highlightthickness= 0, command= new_word)
wrong_button.grid(row= 1, column= 1)

new_word()



window.mainloop()