import turtle
import pandas

screen = turtle.Screen()
screen.title("u.s.states Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guess_state = []


while len(guess_state)<50:
    answer_state= screen.textinput(title=f"len{len(guess_state)}/50 states correct",
                                  prompt="what's anther state's name").title()
    if answer_state =="Exit":
        missing_states = []
        for state in all_states:
            if state not in guess_state:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guess_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)






# import turtle
# import pandas
#
# screen = turtle.Screen()
# screen.title("India States Game")
# image = "india.gif"
# screen.addshape(image)
# turtle.shape(image)
#
#
# data = pandas.read_csv("india_state.csv")
# all_states = data.state.to_list()
# guess_state = []
#
# scale_x = 1
# scale_y = 1
# offset_x = 0
# offset_y = 0
#
# while len(guess_state) < len(all_states):
#     answer_state = screen.textinput(
#         title=f"{len(guess_state)}/{len(all_states)} States Correct",
#         prompt="What's another state's name?"
#     )
#     if answer_state is None:
#         break
#
#     answer_state = answer_state.title().replace(" ", "_").replace("&", "and").replace("(", "").replace(")", "")
#     if answer_state == "Exit":
#         missing_states = [state for state in all_states if state not in guess_state]
#         new_data = pandas.DataFrame(missing_states)
#         new_data.to_csv("states_to_learn.csv")
#         break
#
#     if answer_state in all_states and answer_state not in guess_state:
#         guess_state.append(answer_state)
#         t = turtle.Turtle()
#         t.hideturtle()
#         t.penup()
#
#         state_data = data[data.state == answer_state]
#         x = float(state_data.iloc[0]['x'] if 'x' in state_data.columns else state_data.iloc[0]['X'])
#         y = float(state_data.iloc[0]['y'] if 'y' in state_data.columns else state_data.iloc[0]['Y'])
#         x = x * scale_x + offset_x
#         y = y * scale_y + offset_y
#
#         t.goto(x, y)
#         t.write(answer_state.replace("_", " "), align="center", font=("Arial", 8, "normal"))


