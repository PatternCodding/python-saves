# welcome to intermidiate section in python
'''
OOP: object oriented programming.

why learning OOP?
1. very useful under complex code, like our last project on coffee machine 
2. greate in managing allots of relationships
3. greate in tracking a relationship
4. Procedural programming
5. great and help in maintaining a simple relationship in our code


IMAGINE: CREATING A SELF DRIVING CAR
REQUIREMENT:
=> camera module to keep track of what's on the road
=> Lane detection
=> Needs way of navigating, to decide on going to the bank etc
=> Needs fuel management, what should happen when the fuel goes low?

IMAGINE: WORKING WIT TEAMS THAT HAS A SUB-TEAM
  => Who's working on each of these different modules.
  => makes project to be done more easily and quicker
   
   
   WHAT IS AN OBJECT ORIENTED PROGRAMMONG?
   just imagine working as under a big rstaurant all alone!
   well with procedural programming it' veery impossible to run on this business
   what about dividing the jobs into sections, employing workers while you be the manager tellig them wat to do
   such as: Chef, Waiter, Cleaner, at this junction you don't have to tell a waiter how to do his job and others.
   => so it's in this field of OOP, a programming paradignm
   
   
   HOW TO USE OOP   
   => From the previouse example we gave about having the waiter, cleaner and chef.
       HOW To MODULE THEM
       -->waiter moduling: there's probably two things wee have to think of
       1. what it has and
       2. what it does.
       ==> EXPLANATION
       1. IN TERMS OF WHAT IT HAS:
          a. it might have a variable called {is_holding_plate = True} or
          b. tables_responsible = [4,5,6]
          
        2. WHAT IT DOES SUCH AS:
           a. def take_order(table, order):
                  #maybe taking an order to the chef
            b. def take_payment(amount):
                    #add money to the restaurant
    
    therefore this two different things is what makes up an object, which are:
    
            1. attribute === what it has
            2. methods   === what it does
                ===>attributes is basically like a variable that assocciated with a moduled object, such as the waiter
                ===> attributes is just almost thesame thing, as it's a function. It's called a function because its done a particular module
                     just as we need a waiter method to take the order and take money
                     
                     
THerefore see OOP as the process of modelling a real life object that has attributes and methods.
>>> Object is simply a way of combing i piece of data variable and function all together in the same thing.
>>>  We can actually have a multiple objects generated from thesame type.
>>> just like the waiter in our restaurant, we can have more than two to many waiters doing same job.
>>> and this blue-Print in OOP is called a {CLASS}
>>> while the individual functions generated as an {OBJECT}


BLUEPRINT IN OOP {CLASS}:
>> This deals with the color of the car
>> how many wheels it should have
>> what it's mileage.
>> How much fuel it has
>> the ability to drive
>> the ability to break and stop
 
 
>>>>== And it's from this blue print we can manage to generate as many objecs as we wan to have
WHAT TO CODE IS THE {OBJECT}. 
......the code equivalent of what just happened in creating a new object in python looks like this:
>>> car = carBluePrint() 

EXPLANATION:
1. car: this is the mian object (name)
2. carBluePrint(): this is the class which must be written in pascal case, differentiating from other varibales or function

CAR ATTRIBUTES ARE LIKE IN THIS FORM:
car attributes: speed = 0, fuel  = 32
Now to access those attributes we use a dot 

ACCESSING THE ATTRIBUTES:

car.speed: this simply means from the object caled car get the attribute called speed.

'''

# creating a tutrtle Grapgics in pyhon
#  this was already loaded in our system the moment we installed pythom, found in a modul

# import turtle
# Patterns = turtle.Turtle() 

# or


# from turtle import Turtle, Screen, distance
# Patterson = Turtle()
# print(Patterson)

# accessing the object methods
# https://docs.python.org/3/library/turtle.html
 
# Patterson.shape("turtle")
# Patterson.color("red")


# Patterson.forward(100)
# Patterson.backward(25)


# what can we do with object?
# this our object called turtle, has screen as an attribute, we then add it while importing it.
# and this Screen has a properties like canvheight and canvwidth

# my_screen = Screen()
# print(my_screen.canvheight)

#as you could noticed that there was another screen that showed up and disapperared. and the canvheight as well showed up.

# now let's make it to only disappear only when it's been clicked on.
# noticed our Patterson showing in the middle of the Screen.
 
# my_screen.exitonclick()




# PYTHON PACKAGES VS MODULES
'''
==> A package is different from a module itself, in the sese that it's a whole bunch of code that other people have written, lots and lots of files all packaged to achieve some sort of goal or purpose.
creating a table in python

https://pypi.org/project/prettytable/

and every package you want to use must be installed.

'''

from prettytable import PrettyTable
table = PrettyTable()
# print(table)

# adding columns in our table, which takes two inputs, one is the name of the field and the data that's going into the table

table.add_column("Student", ["Patterson", "Chinedum", "Ogbonnaya", "Destiney"])
table.add_column("Reg-Number", ["Ebsu/2018/92280", "Ebsu/2018/92280", "Ebsu/2018/92280", "Ebsu/2018/92280"])

# print(table)

# remember we can also change the object attribute. such as the alignment,

table.align = "l"
# table.border = False
table.padding_width = 20
print(table) 
