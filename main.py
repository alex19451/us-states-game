import turtle
import pandas


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
screen = turtle.Screen()
title = screen.title("Find USA states Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []

while len(guessed_states)< 50:

    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")

    if answer in all_states:
        guessed_states.append(answer)
        t=turtle.Turtle()
        t.penup()
        t.hideturtle()
        data_state =  data[data["state"]==answer]
        t.goto(int(data_state.x),int(data_state.y))
        t.write(answer)


    



screen.exitonclick()