# Debugging in python & and how to remove them
# the first person that documented debugging was a lady called GRACE HOPPER
# steps to follow:


'''
1. identify the the problem
2. Reproducing the bug
3. play computer
4. Fix the Errors
5. square erros 
6. print is your friend
7. debugger
this is the website to use whike debugging in python
'''


# Describe Problem and tell me why this function is nit running.
# first debugging.

# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# second debugging.  run the program until u get this below error
# IndexError: list index out of range

# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)  #bcos list start counting from 0
# print(dice_imgs[dice_num])

# Play Computer
# step three, run the code by entering 1994

# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# step four, whenever ur editor any error occurs fix it 1st before going ahead

# age = input("How old are you?")
# if age > 18:
#  print("You can drive at age {age}.")

#  square erros
#Print is Your Friend

# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# https://pythontutor.com/render.html#mode=display

def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])