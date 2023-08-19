import random
import time
from turtle import Screen, Turtle
from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_state_on = True
while game_state_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.segments[0].distance(food) < 15:
        food.goto(random.randint(-250, 200), random.randint(-250, 200))
        snake.extend()
        scoreboard.score_update()

    # Detect collision with walls
    if snake.segments[0].xcor() < -380 or snake.segments[0].xcor() > 380 or snake.segments[0].ycor() < -280 or snake.segments[0].ycor() > 280:
        game_state_on = False
        scoreboard.game_over()

screen.exitonclick()
