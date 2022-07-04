'''{creaing more than one turtle}
{creating two or more turtle at once is possible they can function independently}
{in programming we can say that they are each instances of the object}
{just as human are examples of human object}
{assumming we create a timmy and tommy both can have different attributes}
{now since the above can be done this is known as [state]}
'''

from turtle import Turtle, Screen

# tim = Turtle()
# tom = Turtle()
screen = Screen()
# setting up the screen sizes
screen.setup(width=500, height=400)

# creating a pop up text-input
user_bet = screen.textinput(title="Make your choice bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
print(user_bet)


# tim = Turtle(shape="turtle")
# tom = Turtle(shape="turtle")
# dan = Turtle(shape="turtle")
# marv = Turtle(shape="turtle")
# pet = Turtle(shape="turtle")
# mew = Turtle(shape="turtle")
# making our tim to go to a paticular spot, this takes two paarameters {x and y values}
# '''{x axis goes to the horizontal line while the y axis goes to the vertical line}'''
# tim.penup() 
# tom.penup() 
# dan.penup() 
# marv.penup() 
# pet.penup() 
# mew.penup() 
# # tim.shape("turtle")
# tim.goto(x= -230, y=-120)
# tom.goto(x= -250, y=-130)
# dan.goto(x= -230, y=-140)
# marv.goto(x= -230, y=-150)
# pet.goto(x= -230, y=-160)
# mew.goto(x= -230, y=-170)

y_position = [-70, -40, -10, 20, 50, 80]
'''{as a programmer using loop will be the best option}'''
for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    # adding their individual colors
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y_position[turtle_index])
    # to solve this problem of all the turtles lying at same spot we can create list called y_position above

# next is to make our turtle object to be moving on: this is found in another file called
'''{moving_the_turtle}'''

screen.exitonclick()

