'''
understanding turtle module
{Basic importing modules}
{import turtle}: this simply means the import = keyword while the turtle is the module name
tim = turtle.Turtle()
{from turtle inport Turtle}: with this syntax, we can have many turtle names such without have to include the dot
tim = Turtle()
tom = Turtle()
terry = Turtle()
{from turtle import *}: this will have to import all the modules methods in that particular module.
this has advantages and disavantages: {advantages:} you don't need to to import any other method again
{disavantages:} might confuse with same name of methods and variable names
{Alias modules:}
{import turtle as t}: this simply means we now give t as alias name in short way.

{installing modules:} we can't just import all modules some require you installing it before using it.
{[such as the heroes module we used it ealier]}
'''
from turtle import Screen, Turtle, Screen

timmy_the_turtle = Turtle()

# # changing the turtle shape
timmy_the_turtle.shape("turtle")

# # changing the color
# # https://trinket.io/docs/colors
timmy_the_turtle.color("midnight blue")

# # moving our turtle
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(360)


'''{Excercise1: drawing a square using the turtle}'''

# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)

# using for loop is more easy as a programmer to keep our code dry
# for _ in range(4):      
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)


'''{Excercise2: drawing a dashed line of 10 pieces}'''

# for _ in range(15):        
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()
#     timmy_the_turtle.pencolor("red")


'''{Excercise3: drawing a triangle, square, pentagon. hexagon, heptagon, octagon, nonagon and decagon}
{360 / num_side = angle}
'''

# num_sides = 5
# for _ in range(num_sides):
#     angle = 360 / num_sides
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(angle)

# how do we make this to run from a 3 to 10 side of shapes?

# colours = ["CornflowerBlue", "DarkOrchid", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "chartreuse", "dark red", "yellow", "dark olive green"]
# import random
# timmy_the_turtle.pensize(5)
# def draw_shapes(num_sides):    
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)

         
# for shape_side_n in range(3, 11):
#     timmy_the_turtle.color(random.choice(colours))
#     draw_shapes(shape_side_n)


'''{excercise4: Drawing a Random walk which s used in mathematics}'''

# import random
# colours = ["CornflowerBlue", "DarkOrchid", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "chartreuse", "dark red", "yellow", "dark olive green"]

# # making our turtle to be facing different directions.
# '''{ east west north and south}'''

# directions = [0, 90, 180, 270]
# # adding width or pensize to our timmy
# timmy_the_turtle.pensize(5)
# # specifying the speed og our timmy. this can be done by specifying it through the following
# '''{"fastest":0, "fast":10, "normal":6, "slow":3, "slowest":1}'''
# # timmy_the_turtle.speed(0)
# # or
# timmy_the_turtle.speed("fastest")

# for _ in range(100):
#     timmy_the_turtle.color(random.choice(colours))
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.setheading(random.choice(directions))



screen = Screen()
screen.exitonclick()



