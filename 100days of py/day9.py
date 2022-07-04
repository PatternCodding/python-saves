'''
python dictionaries and nesting


What is dictionaries in python? well they are essentially used in collection of related items
which has two parts and they are keys and value paires seperated by comas
'''
programming_dictionary = {"Bug": "An error in a program that prevent the program from running as expected.",
"Function":"A piece of code that you can easily call over and over again.",
"Loop": "The action of doing something over and over agan"
}

# Accesing dictionaries items through the key
# print(programming_dictionary["Bug"])

# trying to add a new entry in dictionary

programming_dictionary["programmer"] = "Someoe who is ready to sit for many hours and came out with jus one or two results."

# print(programming_dictionary)

# creating an empty dict..

empty_dict = {}
empty_dict["love"] = "whatever i like more to add"

# print(empty_dict)

# wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# editing an item in dictionary
programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

# looping throug a dictionary
# trying to use for loop to loop through the items
# for items in programming_dictionary:
    # print(items) # well this can only print out the keys in the dictionary, how can we then solve this issue?

# lets try this aspect

# for key in programming_dictionary:
    # print(key) 
    # print(programming_dictionary[key])

# excercise
'''
from the below student scores, write a program that will convert their scores to grade, by the end of the program
you should have a new dictionary called student_grades that should contain student names for keys and their grades.

if the scores from 91-100 = Outstanding
if the scores from 81-90 = Exceed Expectations
if the scores from 71-80 = Acceptable
if the scores from 70 down = fail
'''

# solution
student_scores = {
    "Patterson": 100,
    "friday": 76,
    "blessing": 80,
    "denis": 60,
    "Chinedum": 99,
    "favour": 81,
}

student_grade = {}

for student in student_scores:
    # print(student)
    score = student_scores[student]
    if score > 90:
        student_grade[student] = "Outstanding"

    elif score > 80:
        student_grade[student] = "Exceed Expectations"

    elif score > 70:
        student_grade[student] = "Acceptable"

    else:
        student_grade[student] = "Fail"

# print(student_grade)


# Nesting in dictionary: this is just the process of putting items one to other.

# this below shows the number of countries i have visited using nested value
# travel_log = {
#     "france": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }

# now assuming i want to as well add the numer times i have visited them, and total number of time i visited them

# travel_log = {
#     "france": {"city_visited": ["Paris", "Lille", "Dijon"], "total_visited": 100},
#     "Germany": {"city_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visited": 10},
# }
# print(travel_log)

# nestng a list, but not that good


# nesting a dictionary inside a list

travel_log = [
     {"country": "france", 
     "city_visited": ["Paris", "Lille", "Dijon"],
      "total_visited": 100},
     {
     "country": "Germany", 
     "city_visited": ["Berlin", "Hamburg", "Stuttgart"], 
     "total_visited": 10
     },
]
# print(travel_log)

# building a biddng in 4G auction under way program

# from replit import clear
bids = {}
bidding_is_finish = False

def highest_bidder(bidder_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Patterson": 678, "Chima": 234}
    for bidder in bidder_record:
        bid_amount = bidder_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"the winner is {winner} with a bid of {highest_bid}")

while not bidding_is_finish:
    name = input("What is your name? ")
    price = int(input("What if your price? $"))
    bids[name] = price
    should_conitnue = input("Are there any other bidders? Type 'yes', else 'no' to quite.")
    if should_conitnue == "no":
         bidding_is_finish = True
         highest_bidder(bids)
    # elif should_conitnue == "yes":
        #  clear()