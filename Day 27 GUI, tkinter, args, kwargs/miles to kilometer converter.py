from tkinter import *

window = Tk()
window.title("Mile to Km converter")
window.minsize(width= 200, height= 200)
window.config(padx= 20, pady= 40)

label_mile = Label(text= "Miles", font= ("Arial",16))
label_mile.grid(column= 10, row=0)

label_km = Label(text= "Km", font= ("Arial",16))
label_km.grid(column= 10,row= 10)

label_is_equal_to = Label(text= "is equal to", font= ("Arial",16))
label_is_equal_to.grid(column= 2,row= 10)

label_result = Label(text= "0", font= ("Arial",16,"bold"))
label_result.grid(column=5, row=10 )


input = Entry(width= 10)
input.grid(column= 5, row=0)
input.focus

## 1 mile = 1.609 km
def mile_to_km():
    miles = float(input.get())
    km = 1.609 * miles
    label_result.config(text= km)

calc_button = Button(text= "Calculate", command= mile_to_km)
calc_button.grid(column= 5,row= 20)




window.mainloop()