# Michael Bunch
# Day 22 of 100 days challenge PONG
# Start 6/3/23
# Finished

from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

paddle = Paddle()

screen.listen()
screen.onkey("Up")
screen.onkey("Down")

screen.exitonclick()