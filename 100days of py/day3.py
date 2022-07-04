# control flow
# overfow: this actually deals with conditional statement,
#  process commanding and given a command on what to do, 
# usin the following:
# if: statement, elseif or elif: and else statement.
'''
before we go into controlflow we should first of all understand some
operators that we will be using, and they are called"
Comparism Operators.

Operators                    Meanings

>                            Greater than
<                            less than
>=                           greater than or equal to
<=                           less than or equal to
==                           equal
!=                           not equal
'''
# print("welcome to basketball game!")
# height = int(input("what is your height?"))

# if height >= 120:
#     print("you can play basketball with us")
# else:
#     print("sorry! you have to grow taller before you can play")


'''
Assignment:
white a python program that will determine if a number user enterd is an even or odd number
'''

# solution

# height = int(input("enter any number "))

# if height % 2 == 0:
#     print("yeah! the number you entered is an even number ")

# else:
#     print("this number is not an even number. ")


# nested if statement
# syntax
# if condition:
#     do this
#     if another condition:
#         do this one
# else:
#     do this particular one 

# print("welcome to nested if else statemet")

# height = int(input("enter your height "))

# if height >= 120:
#     print("yeah! you can play the game ")
#     age = int(input("enter your age"))
#     if age <= 12:
#         print("you can pay $10 ticket.")
#     elif age <=  17:
#         print("you can pay $20 ticket")
#     else:
#         print("you are an adult and your ticket is $120")

# else:
#      print("Sorry! you need to grow more taller to play this game. ")



'''
# Assignment.

write a program that will tell a user that a year he/she entered is a leep year or ot

tip

a year that is divible by 4 without a remainnder is a leep year
except if its evenly divible by 100
unless the year is also evenly divisible by 400
'''
# Solution

# years = int(input("Enter any year you want to check if its a leep year or not\n"))

# if years %4 == 0 & years  % 100 == 0 & years %400 ==0:
#     print("the year you just entered is a leep year!")

# else:
#     print("the year you entered is not a leep year")

# OR

# if years %4 ==0:
#     if years %100 ==0:
#         if years %400 == 0:
#             print("Leap year")
#         else:
#             print("Not a leap year")
# else:
#     print("not a leap year")      



# Multiplt condition
# bill = 0
# print("welcome to basketball academy")
# height = int(input("Enter your height"))

# if height >= 120:
#     print("you can be registered")
#     age = int(input("enter your age"))
#     if age <= 12:
#         bill = 3
#         print("your ticket is $10")
#     if age <= 17:
#         bill = 5
#         print("your ticket is $15")
#     elif age >= 18:
#         bill = 12
#         print("you are already an adult and your ticket is $50")

#     photo = input("do you want a photo taker before or while playing? Yes or No ")
#     if photo == "Yes":
#         bill += 3 
#         # or bill = bill + 3
#     print(f'Your total photo bill is {bill}')

# else:
#     print("sorry! you need to grow more taller")

'''
Asignment

create an authomatic pizz piss project, that would allow a user to request for a pizza.
and this pizza is of different sizes and they are as followed with there prices:
1. small pizza = $15
1. medium pizza = $20
1. large pizza = $25
and ask the user if he would like an extra of the following:
pepperoni for small pizza = $2
pepperoni for medium or large pizza = $3
'''

# print("welcome to python authomatic pizza order!")
# sizes = input("What size would you like to order? S, M, L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N")

# bill = 0
# if sizes == "S":
#     bill += 15

# elif sizes == "M":
#     bill +=20

# else:
#     bill +=25

# if add_pepperoni == "Y":
#     if sizes == "S":
#         bill +=2

# if extra_cheese == "Y":
#     bill +=1
 
# print(f"Your final bill is {bill}")


"""
Logical operators:
this include the following:
1. and ie &: this implies that both must be true
2. or ie |: this implies that either one must be true
3. not : this reverse the opposite
"""
# excercise
# create a program that will would give you ahead order
#  if your grade is A and your age is above 18


# write a program that will ask for your name and your love name.
# then calculate how many true and love occured in the input.

# TIPS: you must use a count() function to know how many the later appered
# and check if both of you are meant for each other! 

# Note make sure you convert everthing to lowercase

# example
# full_name = "Ama Chinedum patterson".lower()
# full_name = input("Enter letters").lower()
# lowe_case = full_name.count('a')
# print(full_name)
# print(lowe_case)


# SOlution

# print("Welcome to Love Calculator!")
# name1 = input("What Your Name? \n")
# name2 = input("What their Name? \n")

# combine_string = name1 + name2
# lower_string = combine_string.lower()

# t = lower_string.count("t")
# r = lower_string.count("r")
# u = lower_string.count("u")
# e = lower_string.count("e")

# true = t + r + u + e

# l = lower_string.count("l")
# o = lower_string.count("o")
# v = lower_string.count("v")
# e = lower_string.count("e")

# love = l + o + v + e

# love_score = int(str(true) + str(love))

# # print(love_score)
# if (love_score < 10) or (love_score > 90):
#     print(f"Your love score is {love_score}, you go together like bread and butter")

# elif (love_score >= 40) and (love_score <= 50):
#     print(f"your score is {love_score}, you are alright together")

# else:
#     print(f"Your score is {love_score}")  



# CREATING A GAME

print('Welcome to treasure island.')
print("your Mission is to find a treasure.")
choice1 = input('you\'re at a crossroad, where do you want to go? type "left" or "right".').lower()

if choice1 == "left":
    choice2 = input('you have come to a lake. There is an island in the middle of the lake. type "wait" to wait for a boad. type "swim" to swim across.').lower()
    if choice2 == "wait":
      choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. which color do you choose? ").lower()
      if choice3 == "red":
          print("its a room full of fire. game over")
      elif choice3 == "yellow":
          print("You find the treature, you win")
      elif choice3 == "blue":
          print("the room is full of hungry lions. game over")
      else:
          print("choice does not exist. Game")

       
    else:
        print("You go attarked by an angry crocodile! game over")

else:
    print("You fell into a hole. Game over")        