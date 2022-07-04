from re import A
from art import logo, vs
from game_data import data
import random
import os
clear = lambda: os.system('cls')



# format the account data into a printale format
def format_data(account):
    accont_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{accont_name}, a {account_descr}, from {account_country}"

# If Statement to check if user is correct
def check_answer(guess, a_followers, b_followrs):
    """Well this can be done in different ways, first way is"""
    # if a_followers > b_follow_account:
    #     if gues == "a":
    #         return True
    #     else:
    #         return False
    """another way, which is the easiest way is"""
    if a_followers > b_follow_account:
        return gues == "a"
    else:
        return gues == "b"


# display logo
print(logo)
score = 0

# adding our while-loop, which comes after testing our code,
# then add game_should_continue = False under the conditional statement in the if is_correct
game_should_continue = True
account_b = random.choice(data) 

while game_should_continue:

    # # Generate a random account from game data
    # account_a = random.choice(data)
    # account_b = random.choice(data)
    
    # 
     # Generate a random account from game data
    account_a = account_b 
    # just to make sure they;re not thesame, then take the account_b = random.choice(data) above
    # what of if the previouse question beccomes the next one, making them thesame, solution
    # change the if statement to while-loop
    # if account_a == account_b:
    #     account_b = random.choice(data)
        
    while account_a == account_b:
        account_b = random.choice(data)
        

    print(f"Compare A: { format_data(account_a)}.")
    print(vs)
    print(f"Against B: { format_data(account_b)}.")


    # Ask user for a guess.
    gues = input("Who has more followers? Type 'A' or 'B': ").lower()



    # Check if user is correct.
    ## Get follower count.

    a_follow_account = account_a['follower_count']
    b_follow_account = account_b['follower_count']
    ## If Statement to check if user is correct, let's jus use function to make it re-usable

    """calling the function created above"""
    is_correct = check_answer(gues, a_follow_account, b_follow_account)
    
    # adding a clear function, after importing the os at the begining of this project
    # pr oblem is that the vs logo dissappear after clearing.
    # solution is print the logo after printing  after clearing
    clear()
    print(logo)
    # Give User feedback on their guess. and
    # keep track of our game, by setting the score = 0, below print(logo)
    if is_correct:
        score +=1
        print(f"You got it correct! Current score is {score}. ")
    else:
        game_should_continue = False
        print(f"Sory, that's wrong. Final score is {score}")

    # now test the coe finding out that we need while-loop to continiue playing
    # it' important to figure out whih part of the code need to be repeated. after score = 0






'''

FAQ: Why does choice B always become choice A in every round, even when A had more followers? 

Suppose you just started the game and you are comparing the followers of 
A - Instagram (364k) to B - Selena Gomez (174k). Instagram has more followers,
so choice A is correct. However, the subsequent comparison should be between Selena
Gomez (the new A) and someone else. The reason is that everything in our list has fewer
followers than Instagram. If we were to keep Instagram as part of the comparison
(as choice A) then Instagram would stay there for the rest of the game. This would be
quite boring. By swapping choice B for A each round, we avoid a situation where the
number of followers of choice A keeps going up over the course of the game. Hope that
makes sense :-)

'''




# Generate a random account from the game data.

# Format account data into printable format.

# Ask user for a guess.

# Check if user is correct.
## Get follower count.
## If Statement

# Feedback.

# score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.