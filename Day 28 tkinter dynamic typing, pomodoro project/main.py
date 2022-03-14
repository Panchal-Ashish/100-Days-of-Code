from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
ORANGE = "#FFC107"
BLUE ="#39A2DB"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_display = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer_display)
    canvas.itemconfig(timer_text, text = "00:00")
    title.config(text= "Timer")
    checkmark.config(text="")
    global reps
    reps = 0





# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 8:
        title.config(text=f"Long break of {LONG_BREAK_MIN} mins", fg= ORANGE)
        countdown(long_break_sec)
    elif reps % 2 == 0:
        title.config(text=f"short break of {SHORT_BREAK_MIN} mins", fg= ORANGE)
        countdown(short_break_sec)
    elif reps % 2 != 0:
        title.config(text=f"work for {WORK_MIN} mins", fg= ORANGE)
        countdown(work_sec)





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global checks
    count_min = math.floor(count/60)        # it removes all digits after the decimal... rounds to previous integer
    count_sec = count % 60      # Modulo operator (%) returns the remainder
    if count_sec == 0 or count_sec <10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")
    if count > 0:
        global timer_display
        timer_display = window.after(1000,countdown, count - 1)
    else:
        start_timer()
        checks = ""
        for _ in range(math.floor(reps/2)):
            checks += "✔"
        checkmark.config(text=checks)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro timer")
window.config(padx=10, pady=50, bg=YELLOW)



## CANVAS ##
canvas = Canvas(width=200, height=225, bg=YELLOW, highlightthickness=3)

img = PhotoImage(file="C:/Users/Manoj/PycharmProjects/Udemy 100 days of code"
                      "/Day 28 tkinter dynamic typing, pomodoro project/tomato.png")
canvas.create_image(100, 112, image=img)    # do not write x , y as they are args... not keyword arguments
## does not take the image file path directly like we did in turtle background image...
## so,'PhotoImage' is a class in tkinter to read through the image file location... which can then be passed into canvas

timer_text = canvas.create_text(100, 130, text="00:00",fill= "white", font= (FONT_NAME,36,"bold"))
## canvas cannot be modified by config method like label... instead
## use syntax: canvas.itemconfig(canvas item to configure, thing to configure)
canvas.grid(column=1, row=1)



## BUTTONS
start = Button(text= "start", command= start_timer)     ## buttons can have width
start.grid(column= 0, row= 3)

reset = Button(text= "Reset",command= reset_timer)
reset.grid(column= 2, row= 3)

# LABELS
title = Label(text="Timer", fg= BLUE, bg= YELLOW, font= ("arial", 28, "bold"))  ## labels do not have width
title.grid(column= 1, row= 0)

checkmark = Label(text= "", fg= BLUE, font= ("arial",14,"bold"))
checkmark.grid(column= 1, row= 2)


window.mainloop()