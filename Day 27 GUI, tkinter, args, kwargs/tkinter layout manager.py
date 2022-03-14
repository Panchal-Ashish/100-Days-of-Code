## PACK, PLACE, GRID
#PACK simply places it centre by default
#PLACE requires x and y coordinates (keyword arguments)
#GRID... considers a grid layout...NOTE ... all grid coordinates are relative to the first grid coordinate used wherever

## grid and pack cannot be used in same code together
from tkinter import *

window = Tk()
window.title("layout manager")
window.minsize(width= 500, height=300)


# label
my_label = Label(text="I am a label",font= ("arial",24,"bold"))
# my_label.pack()
# my_label.place(x=0,y=0)
my_label.grid(row= 0, column= 0)


# Button
def button_clicked():
    print("I was clicked")

button = Button(text = "click me", command= button_clicked)
# button.pack()
# button.place(x=30,y= 60)
button.grid(row= 5, column= 10)

# entry
input = Entry(width=10)
print(input.get())
# input.pack()
input.place(x= 50,y= 150)
# input.grid(row= 10, column= 20)


window.mainloop()
