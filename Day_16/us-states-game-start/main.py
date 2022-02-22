import turtle

screen = turtle.Screen()
screen.title("US State Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

def get_mouse_click_coor(x, y):
    print(x, y)

answer_state = screen.textinput(title="Guess the State", prompt="Whats another states name")
print(answer_state)



turtle.mainloop()

