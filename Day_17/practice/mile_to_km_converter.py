import tkinter 

window = tkinter.Tk()
window.title("Miles to km converter")
window.minsize(width=200, height=100)


#Miles label
miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2,row=0)

#km Label
km_label = tkinter.Label(text="km")
km_label.grid(column=2, row=1)

#km answer label
km_answer_label = tkinter.Label(text="0")
km_answer_label.grid(column=1,row=1)


#Equal to label
equals_label = tkinter.Label(text="is equal to ")
equals_label.grid(column=0,row=1)
#calculate button 

# text input button 
miles_input = tkinter.Entry()
miles_input.grid(column=1,row=0)


#caluclate button 
def button_clicked():
    km_answer_label["text"] = int(miles_input.get()) * 1.60934
button = tkinter.Button(text="Calculate",command=button_clicked)
button.grid(column=1,row=3)

window.mainloop()
