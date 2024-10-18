import turtle
from turtle import Screen, Turtle, write
import random

is_racing = False
turtle.hideturtle()
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which color will win the race?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

def make_turtles():
    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=y_position[turtle_index])
        all_turtles.append(new_turtle)

def move_turtles():
    for t in all_turtles:
        t.forward(random.randint(0, 10))
        if is_win(t):
            break

def is_win(t):
    global is_racing
    if t.xcor() >= 230:
        is_racing = False
        winning_color = t.pencolor()
        # print(f"You've {'won' if winning_color == user_bet else 'lost'}! The {winning_color} turtle is the winner!")
        print_winner(winning_color)
        return True
    return False

def print_winner(color):
    if color == user_bet:
        winner_message = "You've won! The {winning_color} turtle is the winner!"
    else:
        winner_message = "You've lost! The {winning_color} turtle is the winner!"
    write(winner_message.format(winning_color=color), align="center", font=("Arial", 18, "bold"))

if user_bet:
    is_racing = True

make_turtles()
while is_racing:
    move_turtles()

screen.listen()
screen.exitonclick()