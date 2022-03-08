from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers=['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!','#','$','%','&','(',')','+']

    nr_letters = random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)

    password_list = []

    password_letters = [random.choice(letters) for letter in range(nr_letters)]
    password_numbers = [random.choice(numbers) for number in range(nr_numbers)]
    password_symobls = [random.choice(symbols) for symbol in range(nr_symbols)]
    password_list = password_letters + password_numbers + password_symobls

    random.shuffle(password_list)
 
    password = "".join(password_list)
    password_input.insert(0, password)
    # pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    user = user_input.get()
    password = password_input.get()

    is_ok = messagebox.askokcancel(title=website, message="These are the details entered: \n Email:{}, \n Password: {}\nIs it ok to save?".format(user, password))
    
    if is_ok: 
        if len(password) == 0 or len(webiste) ==0 or len(user)==0:
            messagebox.showerror(title=website, message="This filed is required") 
        with open("data.txt", "a") as data:
            data.write("{}, {}, {} \n".format(website, user, password))
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(row=0,column=1)

# Adding webiste label
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

# Adding user label
user_label = Label(text="Email/Username:")
user_label.grid(row=2,column=0)

#Adding password label
password_label = Label(text="Password:")
password_label.grid(row=3,column=0)



#Adding website text box
website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

#Adding user text box
user_input = Entry(width=35)
user_input.insert(0,"sanjnac@gmail.com")
user_input.grid(row=2, column=1, columnspan=2)

#Adding password text box
password_input = Entry(width=18)
password_input.grid(row=3, column=1)

# save(website_input.get(), user_input.get(), password_input.get())

#Adding generate password button
gen_pass_button = Button(text="Generate Password", command=generate_password)
gen_pass_button.grid(row=3, column=2)

# Adding add password button
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()