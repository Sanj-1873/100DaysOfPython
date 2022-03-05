from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps 
    reps = 0
    start_timer()
    # pass
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps 
    reps += 1

    work_sec = WORK_MIN * 60 
    short_break_sec = SHORT_BREAK_MIN * 60 
    long_break_sec = LONG_BREAK_MIN * 60 

    if reps % 8 == 0: 
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)

    elif reps % 2 == 0: 
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=RED)

    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    mins = math.floor(count/60)
    secs = count % 60
    if secs < 10:
        secs = "0" + str(secs)
    if mins <10:
        mins = "0" + str(mins)

    canvas.itemconfig(timer_text, text="{}:{}".format(mins, secs))
    if count > 0:
        window.after(1000, count_down, count-1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)



#Adding the tomato image 
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1,column=1)



#Adding the timer label 
timer_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

#Adding the start button
start_button = Button(text="Start", command=start_timer, bg=YELLOW, font=(FONT_NAME,12))
start_button.grid(row=2, column=0)

#Adding the reset button 
reset_button = Button(text="Reset", command=reset_timer, bg=YELLOW, font=(FONT_NAME,12))
reset_button.grid(row=2, column=2)
window.mainloop()

#Adding check mark label 
check_label = Label(text="✓", fg=GREEN, bg=YELLOW)
check_label.grid(row=3, column=1)
