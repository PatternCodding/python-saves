"""
OUTLINES:
code blocks
function
while loops
"""

# FUNCTIONS IN PYTHON
# there are many python functions, len, int, print, range etc..
# why are they fuctions?
# with parentheses

# OUR OWN FUNCTION

# synatax

# def function_name():
    # body of function, and its definitions
    # 
    # 
# triggering function 

# example
# def my_function():
#     print('the addition of ', 1+2 , 'is')

# my_function()

 
# def calculation(n1, n2):
#  print(n1 * n2)


# calculation(12, 45)

# def fullname(fname, lname):
#     print(fname + " " + lname)

# fullname("Chinedum", "Patterson")

# indentation.
"""
its advisable to understand python indentation, as it only woks out for you oncce the indentation is on it cagtegory.
else always give at least give 4spaces in a function, you can use tab to create a space, but 
spaces is the most useful one, but thanks to many editors once you click on enter it authomatically jumps into 4spaces
"""

# WHILE LOOP
# this is an a boolean observer, apply while the condition is true, stop while its fault

# numbers = 0
# while numbers < 10:
#     print(numbers)
#     numbers +=1


'''
note: while loop is not like for loop, in the area of for loop, you already know how many times youre going to loop through,
while in while loop, its only going to stop once it reaches it demands


avoid infinite loop.
by saying while 5 > 3
'''

# the break statement:

# i = 1
# while i < 10:
#     print(i)
#     if i == 2: 
#        break
#     i += 1


# the Continuestatment

# num = 0
# while num < 10 :
#     num +=1
#     if num == 3:
#         continue
#     print(num)
# # adding else statement
# else:
#     print("its finished")


'''
PROJECT IS TO CREATE A HANGMAN GAME... go wikipedia and find more about the hangman game
'''

# STEP 1
import random

word_list = ['ardvark', 'baboon', 'camel']
chosen_word = random.choice(word_list)
word_lenght =  len(chosen_word)


# testing code
print(f"pssst, the solution is {chosen_word}.")

# TODO-1- randomly choose a word from word_list and assign it to a variable called chosen_word
# create an empty list called disply.
# for each letter in the choosen_word, add a "_" to 'display'.
# so if the chosen_word was "apple", display should be ["_", "_", "_", "_", with 5"_", representing each
# letter to guess.]


# TODO-2- Ask the user to guess a letter and assign their answer to a variable called guess.
# make guess lowercase().

# empty letter word
display = []
# for letter in chosen_word: # u can replace the letter with _
# lets use range instead.
for _ in range(word_lenght):
    display += "_"
# print(display ) 


guess = input("Guess a letter ").lower()
'''
step 2
loop through each position in the chosen_wod. if the letter at the position matches 'guess', then
reveal that letter in the display at the position.
e.g if the user guessed "p" and the chosen word was 
"apple", then display should be ["_", "p", "p", "_", "_" ]
'''
# for letter in chosen_word:
#     if letter == guess:
#         print("right")
#     else:
#         print("wrong")
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter ").lower()
    #   check guessed letters
    for position in range(word_lenght):
        
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

 
print(display )
if "_" not in display:
    end_of_game = True
    print("You win")
# TODO-3- check if the letter the user guessed (guess) is one of the letters in the chosen_word
'''
print 'display' and you should see the guessed letter in the correct positio ans every other letter
replace with "_".
HINT - dont worry about getting the user to guess the next letter,
we will tackle that togeter in step 3
'''




