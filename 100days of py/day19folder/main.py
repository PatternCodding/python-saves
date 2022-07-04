'''{Event listener in python turtle}'''

'''{example of a higher order functionis}'''
# def add(n1, n2):
#     return n1 + n2

# def sub(n1, n2):
#     return n1 - n2

# def mult(n1, n2):
#     return n1 * n2

# def divide(n1, n2):
#     return n1 / n2

# def calculator(n1, n2, func):
#     return func(n1, n2)

# result = calculator(2, 3, add)

# print(calculator)

from turtle import  Turtle, Screen

tim = Turtle()
screen = Screen()

# for us to start listening we need to hold  of the screen object and then tell it to start listening.

# def move_forward():
#      tim.forward(10)
     

# screen.listen()

# once it start listening we need to bind a function thay will be triggered when 
# a particular key is pressed on the keyboad, such as onkey

# screen.onkey(key="space", fun=move_forward) 
#do not add a parenthesis to a function you want to pass to another like this.
# this kind of function is called a higher order function.
# thi is the kind of function that can work with other functions
# screen.exitonclick()


# Excercise use the idear you've gotten from this lesson, create aturtle program that will display the following:
'''
W = forward
S = Backword
A = Counter_Clockwise
D = clockwise
C = clear drawing and go back defult
{remember that the event does not recieve and argument}
'''
# solution

def move_forward():
     tim.forward(10)
     
def move_backword():
     tim.backward(10)
     
def turn_left():
     new_heading =  tim.heading() + 10
     tim.setheading(new_heading)
    #  or
    #  tim.left() + 10

     
def turn_right():
     new_heading =  tim.heading() - 10
     tim.setheading(new_heading)
    #  or
    #  tim.right() -m10
    
def clear():
    tim.clear()
    # bringing tim back to the center at the starting point using a method called home. note if you don't allow tim
    # to put his pen up it will draw another line while going back.
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward) 
screen.onkey(key="s", fun=move_backword) 
screen.onkey(key="a", fun=turn_left) 
screen.onkey(key="d", fun=turn_right) 
screen.onkey(clear, "c") 

screen.exitonclick()