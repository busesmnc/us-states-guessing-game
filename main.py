import pandas
import turtle
import csv

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# to find positions of the states, used get_mouse_click_coord function,
# results were already added to te list 50_states.csv
# def get_mouse_click_coord(x, y):
#     print(x, y)
# tomy.onscreenclick(get_mouse_click_coord)


data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()

print(all_states)
score = 0
game_on = True
correct_ans = []

while game_on:

    answer_state = screen.textinput(title=f"{score}/50 States Correct",
                                    prompt="What's another state's name?").title()
    print(answer_state)

    if answer_state.lower() == "exit":
        unknown_states = []

        for i in range(len(all_states)):
            if all_states[i] not in correct_ans:
                unknown_states.append(all_states[i])

        new_data = pandas.DataFrame(unknown_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        score += 1
        correct_ans.append(answer_state)
        state = data[data.state == answer_state]
        tomy = turtle.Turtle()
        tomy.penup()
        tomy.hideturtle()
        tomy.goto(int(state.x), int(state.y))
        tomy.write(answer_state)

    if len(correct_ans) >= 50:
        game_on = False


turtle.mainloop()

#  instead screen.exitonclick() used tomy.mainloop()
