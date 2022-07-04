# Randomisation and python list
# randomisation simply means the process in which computer would be able to gie you psuedo random generators
# for more detail visit {pyhonask.com}


# random is a module, this is like a division of code created to help in a particular purpose.
# and as well for an easy achievement while coding
# there modules has already been created either by the language creator
# or by a language user (programmer)
# exampls is creating and external file then importing it for ur curret coding
# the type of psuedo random python uses is whats is called [mersenne Twister.go onlne for more details]

  
import random

randtint = random.randint(1, 10)
# print(randtint)
 
# creating a random floating numbers
rand_float = random.random()
# of course its generating numbers from 0.0> - 0.999
# how then do we parse a value for its specializations?
rand_float = random.random() * 5
# print(rand_float)



# what can we do random numbers? 
# can be used in many stuffs, dice, games, etc

lova_score = random.randint(10, 100)
# print(f"   Your love score is {lova_score}")

# excercise:
'''
write a program
'''

# randome_side = random.randint(1,0)
# if randome_side == 1:
#     print("heads")

# else:
#     print("Tail")




# PYTHON LIST: This is called a data structure.
# storing group pieces of data.
# they are mutable
# they are an order way of storing values
# uses [], storing related items
# can contain anything seperated by a coma

states_in_nigeria = ["Abia", "Ebonyi", "lagos", "Imo"]

# accessing list items

# [] and its index
# print(states_in_nigeria[0])


# changingan iten in the list
states_in_nigeria[3] = "Anambra"

# adding an item in the list at the end

states_in_nigeria.append(['ogun', "kebi", "enugu"])
# you can as well use extend,
# print(states_in_nigeria)

# there are many list method in python:
# pop(), insert(), remove() and many more, you can get them on google

# introduction to split:
# this is use to split some strings into the programmers choice
#  example
my_split = 'hello mr chinedum ogbonnaya'
# print(my_split.split())
# print(my_split.split(","))
'''
{ASSIGNMENT}
write a program that would pick a particular
whos is going to pay a bill from the list of friends
whom went in a retaurat to eat, and print out the particula
that was picked
'''

# SOLUTION

# friends_names = input("Write down your friends name, sepersted with a coma!\n")
# names = friends_names.split(", ")

# of couse we can pick up a particular index to pay the bill
# print(names[0])

# but how do we do that using random? and at same time how do 
# we know the end of the index??

# solution

# num_items = len(names)
# random_choice = random.randint(0, num_items - 1)
# payer = names[random_choice]
# print(payer + " is going to pay the meal today")
 

# OR. shortest way to do it:
# payer = random.choice(names)
# print(payer + " is going to pay the meal today")

# More on list
states_in_nigeria = ['ogun', "kebi", "enugu", 'anambra', 'bauchi', 'bayesa']

# asuming you want to print the last state of unkown.

state_len = len(states_in_nigeria)
# print(state_len[-1])


# nexted list

# myList1 = ['strawberry', 'grapes', 'peaches', 'pears', 'spinach', 'tomatoes']

# myList2 = ['mangoes', 'apples', 'celery', 'potatoes']

# fruits = [myList1, myList2]
# # print(fruits)


# creating a boad with list

row1 = [" ",  " ", " "]
row2 = [" ",  " ", " "]
row3 = [" ",  " ", " "]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")



# position = input("Where do you want to put the treasure? ")





# horizontal = int(position[0])
# vetical = int(position[1])

# selected_row = map[vetical - 1]
# selected_row[horizontal - 1] = "X"

# print(f"{row1}\n{row2}\n{row3}")


# rock paper and scissor game
rock = '''
------"__
      '___;
      '___;
      '___;
    ' __'
'''
paper = '''
------"__
      '___;
      '___;
      '___;
    ' __'
'''
scissors = '''
------"__
      '___;
      '_____
      '_____;
    ' __'
'''
game_images = [rock, paper, scissors ]

user_choice = int(input("make a choice, 0 for rock, 1 for paper and 2 scissors\n"))

if user_choice >= 3 or user_choice < 0:
    print("You chosed an invalid number, You lose")

else:
        
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print(f"Computer chose:")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("you win")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose!")
    elif user_choice > computer_choice: #this line of code will actually terminate the else statement
        print("You win")
    elif computer_choice == user_choice:
        print("Its a draw!")   
    # else:
    #     print("Invalid input, you lose")
    # elif user_choice >= 3 or user_choice < 0: #this would still not solve the problem
    #     print("You chosed an invalid number, You lose") #for that we move it upward