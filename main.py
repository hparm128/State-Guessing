import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")

guessed_states = []
all_states = data["state"].to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state?").title()
    if answer_state == "Exit":
        break
    if answer_state in guessed_states:
        continue
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

if len(guessed_states) < 50:
    remaining_states = [state for state in all_states if state not in guessed_states]
    new_data = pandas.DataFrame(remaining_states)
    new_data.to_csv("remaining_states.csv")


screen.exitonclick()
