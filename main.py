import time
from turtle import Screen, Turtle

screen = Screen()

screen.setup(width=500, height=400)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

starting_position = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

screen.update()

game_state_on = True
while game_state_on:
    screen.update()
    time.sleep(0.1)
    for segment_num in range(len(segments)-1, 0, -1):
        segments[segment_num].goto(segments[segment_num - 1].pos())
    segments[0].forward(20)
    segments[0].left(90)


screen.exitonclick()
