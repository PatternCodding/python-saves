

# scope. imagine having an apple tree inside your compound, who do you think has the access the to the apple, then plating the apple outside the compound

# enemies = 1

# def  increase():
#     enemies = 2
#     print(f"enemies inside fuction: {enemies}")
    
# increase()
# print(f"enemies outside fuction: {enemies}")
    
    
# local cope, exist within a function

# def drink_potion():
#     potion_strenght = 2
#     print(potion_strenght)
    
# drink_potion()

# print(potion_strenght)
# the soulution is called global scope

# block csope in python
# block of code. unlike other languages such as C- families, java and js. there's no such thing called block scope in python, what do i mean?
# if your were to create an if statement, while loop, etc, then creating a variable within it is nor offensive.

# game_level = 3
# enemies = ["skeleton", "Zombie", "Alien"]
# if game_level < 5:
#     new_enemy = enemies[0]
# print(new_enemy)

# you see that the code above has no issue right, desspite the new_enemy vaviable been created within the if block, and printing outside the block? alright the chekck this out with a function

# game_level = 3
# def  create_enemy():        
#     enemies = ["skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]
#     print(new_enemy) # trying to print outside the function
  
  
#the reason been that within the function there's a local scope, so enemy is available within the function. 
# ecause blocks like if, while, for, all of these blocks of code with colons and indentation, they don't count as creating a local scope
  


# How to modify variable within global scope

# enemies = 1
# def  increase():
#     enemies += 2
#     print(f"enemies inside fuction: {enemies}")
    
# increase()
# print(f"enemies outside fuction: {enemies}")
    
    
# trying to modify the above code by just adding global after the function

# enemies = 1
# def  increase():
#     global enemies
#     enemies = 2
#     print(f"enemies inside fuction: {enemies}")
    
# increase()
# print(f"enemies outside fuction: {enemies}")

# avoid modifying global scopes if you're not good in pythin yet, you can rather use return statement, return +=1
    
    
# Python Constant & Global Scope
# Global scope could be useful in a value you wouldin't want to change ever

pi = 3.14159 
def cal():
    pi
    
#Note, the best practice using a global scope is turning everything into uppercase, so that whenever you want to use it and see it in uppercase you'll then
# remember it's global variable you would'nt want to change.


# PI = 3.14159
# URL = "https://ww.google.com"
# TWITTER_HANDLE = "Qme_chinedum"
    

#  final project on this leson.


from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")
      
game()

