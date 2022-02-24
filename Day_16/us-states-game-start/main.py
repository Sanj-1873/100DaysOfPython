import turtle
import pandas 
from states import States

df = pandas.read_csv("50_states.csv")


screen = turtle.Screen()
screen.title("US State Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

def get_mouse_click_coor(x, y):
    print(x, y)


game_is_on = True
correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title="{}/50 correct".format(len(correct_guesses)), prompt="Guess a state")
    if answer_state:
        if answer_state == "Exit":
            break
        answer_state = answer_state.title()
        correct_state = df.state == answer_state

        if correct_state.any():
            
            if answer_state not in correct_guesses:
                correct_guesses.append(answer_state)
            
            # Create turtle writing
            print(correct_guesses)
            
            row = df[df.state == answer_state]
            x_cor = int(row.x)
            y_cor = int(row.y)
            
            state = States(answer_state, x_cor, y_cor)

# States to learn




turtle.mainloop()

