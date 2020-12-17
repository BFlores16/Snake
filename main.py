from turtle import Screen
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard
import time

# Initial screen setup

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Key event listeners for the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
#Keep the game on
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.new_food()
        snake.extend()
        scoreboard.increment_score()

    #Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -295 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.write_game_over()

    #Detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.write_game_over()

screen.exitonclick()
