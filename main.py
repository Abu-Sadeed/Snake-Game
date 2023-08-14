import time
from turtle import Screen, Turtle
from snake import Snake

screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()


game_state_on = True
while game_state_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
