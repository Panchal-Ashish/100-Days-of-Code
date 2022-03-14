from tkinter import *
import time
# creating window similar to turtle screen
window = Tk()
window.title("tkinter intro")

# by default, window has certain default size and will scale to include all elements in the window
# but we can set the size as follows
window.minsize(width=500, height=300)



## creating label in tkinter but is not displayed by default
my_label = Label(text="I am a label",font= ("Times New Roman",24,"bold"))

# my_label["text"] = "I am a label"   # alt 1
# my_label.config(text= "I am a label")   # alt 2


## displaying the label using pack method    # all arguments (eg.side) is optional...kwargs
my_label.pack()


## Button... arguments reqd are kwargs
def button_clicked():
    my_label.config(text = "Button clicked")
    print("I was clicked")


button = Button(text = "click me", command= button_clicked)     #command is the action to be performed on clicking
button.pack()



## entry... arguments reqd are kwargs
input = Entry(width = 10)
input.pack()
print(input.get())      # getting the input and returning it as a string




# keeping the window on screen and listeningand looping lifeime... similar to exit on click in turtle, except it does not exit on clicking
# only method to exit is by cancelling or clicking 'x' button
window.mainloop()
