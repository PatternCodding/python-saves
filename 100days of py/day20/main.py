'''
{we will be using OOP}
{in this section we'll be bilding a snake game, just like the one found in Nokia 3310.}
you should know wenever we're working a big project we're meant to divide them into many modules,
{those problem we are to breakdown into modules are of seven seperate steps:}
1. create a snake body: this is going to be done by creating three square in the screen lying down next to each other.
2. figuring out how to move the snake.
3. figuring out how to control the snake using the keyboad.
4. Detect collision with food to grow
5. Create a scoreboard to update or increamrnt our score 
6. Detect collision with wall (game over)
7. Detect collision with tail or body (game over)
'''



from tracemalloc import start
from turtle import Turtle, Screen
'''{importing time is under second step. comes after screen update}'''
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# to make our snake to more like one, we'll have to turn off the tracer
screen.tracer(0)

'''{first step. Craete a snake body}'''
# segment_1 = Turtle("square")
# segment_1.color("white")

# segment_2 = Turtle("square")
# segment_2.color("white")
# segment_2.goto(-20, 0)

# segment_3 = Turtle("square")
# segment_3.color("white")
# segment_3.goto(-40, 0)
'''{from second step}'''
segment = []
# using for loop instead using python turple
start_position = [(0, 0), (-20, 0), (-40, 0)]
for position in start_position:
    new_segement = Turtle("square")
    new_segement.color("white")
    new_segement.penup()
    new_segement.goto(position)
    '''{second step. Move the snake}'''
    segment.append(new_segement)

# making the snake to contiue going
game_is_on = True
while game_is_on:
    # let's update our screen after turning off the tracer, else nothing will work
    screen.update() 
    time.sleep(0.1)
    # for seg in segment:
    #     seg.forward(20)

    '''{this section comes after sleep}
    {Let us comment the for loop and try to move our snake left or right entirely}
    {this for loop is going to make our snake at position 3 to more to 2 while 2 to to 1 this reverce order }
    '''
    # for seg_num in range(start = 2, stop = 0, step = -1): #not supported in python rather in C family
    for seg_num in range(len(segment) - 1, 0, -1):
        new_x = segment[seg_num -1].xcor()
        new_y = segment[seg_num -1].ycor()
        segment[seg_num].goto(new_x, new_y)
    segment[0].forward(20)
    

screen.exitonclick()