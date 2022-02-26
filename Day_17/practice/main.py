import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label

my_label = tkinter.Label(text="I am a label", font=("Arial", 24))

my_label.pack()

my_label["text"] = "Say Something"
# my_label.config(text="new text")


# Entry

input = tkinter.Entry()
input.pack()

#Button 
def button_clicked():
    my_label["text"] = str(input.get())


button = tkinter.Button(text="Click Me", command=button_clicked)

button.pack()







window.mainloop()