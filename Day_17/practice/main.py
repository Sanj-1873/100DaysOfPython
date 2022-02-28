import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label

my_label = tkinter.Label(text="I am a label", font=("Arial", 24))

my_label.grid(column =0, row =0)
# my_label.pack()
# my_label.place(x=100, y=200)
my_label["text"] = "Say Something"

# my_label.config(text="new text")



# Entry

input = tkinter.Entry()
#input.pack()
input.grid(column=4, row=3)

#Button 
def button_clicked():
    my_label["text"] = str(input.get())
button = tkinter.Button(text="Click Me", command=button_clicked)

#button.pack()
button.grid(column=1, row=2)


#new button 
new_button = tkinter.Button(text="new button")
new_button.grid(column=2,row=1)

window.mainloop()