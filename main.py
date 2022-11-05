# Create a program that emulates a turtle race and takes a bet as input
from turtle import Turtle, Screen
import random

screen = Screen()
# Sets screen dimensions
screen.setup(width=500, height=400)
colors = ["red", "blue", "green", "purple", "orange", "yellow"]
# Creating Contestants
all_turtles = []
y_position = -150
for turtles in range(0, 6):
    y_position += 50
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtles])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position)
    all_turtles.append(new_turtle)

# Creating the game's logic
race_is_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The Winning color is {winning_color}")
            else:
                print(f"You loss! The Winning color is {winning_color}")

        speed = random.randint(0, 10)
        turtle.forward(speed)

screen.exitonclick()
