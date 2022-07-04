# LOOPS in python


'''
To check if your email or password is among those been registred for hacking
held on to ;--have i been pwned.com
'''
# 1) For Loop, under list
# fruits = ["apple", "peach", "pear", "mango"]
# for fruit in fruits:
    # print(fruits)
    # print(fruit)

# assigning another fruit to the list
    # print(fruit + " is a fruit")

# indentation matters allots
# print(fruit + " is a fruit")


'''
{ASSIGNMENT}
whrite a program that will claculate the average students height from
a list of height. e.g, students_height =
[180 124 173 189 169 146],
the average height can be calculated by asking all the height together and dividing
by the total number of height
 the round it to the nearest whole number
'''

# solution
student_heights = input("Enter students heights ").split()
for n in range(0, len(student_heights)):
 student_heights[n] = int(student_heights[n])
print(student_heights)  

"""
of couse with the len() we can get the lenght 
and also the sum() but youre not permitted to use this function to get the result
if we could it would be super easy like:
"""

# total_heights = sum(student_heights)
# number_of_students = len(student_heights)
# average_height = round(total_heights / number_of_students)
# print(average_height)

# but youre to use for loop and solve this problem


# SOLUTION

# this is the sum function solution

total_heights = 0
for height in student_heights:
    total_heights += height
print(total_heights)

# now lets deal with the len function

number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(number_of_students)

# now lets gets the average

average_height = round(total_heights / number_of_students)
print(average_height)



'''
{ASSIGNMENT}:
Write a program that would calculate the height score of list of score
e.g. students score = [78, 65, 89, 55, 91, 64, 89]

IMPORTANT: you are not permited to use max or min function.
the output should look like'
the highest score from the output is :
'''

# SOLUTION
# student_scores = input("Enter students score").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)
 
# higest_score = 0
# for score in student_scores:
#     if score > higest_score:
#         higest_score = score
# print(f"The highest score in the class is {higest_score} ")



# All this while we have been using for loop under a list, lets try it on other ways

'''
there was a teacher who gave one of his students a work to do, hoping to keep im busy
telling him to calculate 1+1-----100, to his greatest suprise before two minutes the small
boy came back with the ansa,... How??

he figured that if you flip the number around.
1+2+3+4+5+.......99+100
100+99+98+97+96.......+3+2+1

he noticed that 1+100 = 101, 2+99 =101 etc
basically if you tie these numbers together there is actually 50 pairs of 101

so  you can simply just do 
50 * 101 which is 5050.

that is how the greatest mathematician figured if out his name is

[Carl Gauss]

but we can do better than him by using LOOP
'''

# for loop with the range function

# syntax
'''
for number in range(a, b):
     print(number)    
'''

# example
# for number in range(1, 10):
#     print(number)

# now assuming you want to increased the step by any other number instead of addition 
# of 1 each time then you specify it within and at the last value in the parenthesis 

# example

# for number in range(1, 10, 2):
#     print(number)

# How do we add up numbers from 1 - 100

# solution

# total = 0
# for number in range(1, 101):
#     # total += number
#     total = number + total
# print(total) 

'''
EXCERCISE: this is always an interview question, its called fizzbuzz

write a program that automatically print the solution to the FizzBuzz game.

Your program should print each number from 1 to 100 in turn.

when the number is divisible by 3, then instead of printing the number, it should
print "Fizz".

when its divisible by 5 prits "Buzz"

when its divisible by both 3 and 5 should print "FizzBzz"

the rules of this game is very simple.

when we sit in a circular form. the 1st person says one followed by the 2nd etc
once a person met a number that is divisible by 3 instead of saying the number should say "Fizz" etc
'''

# solution

# numbers = int(input("Enter any number\n"))
# for number in range(1, 101):
    
#     if number % 3 ==0 & number % 5 ==0:
#         print("FizzBuzz")

#     elif number % 3==0:
#         print("Fizz")

#     elif number % 5 ==0:
#         print("Buzz")  

#     else:
#         print(number )
import random
'''
How to generate a password by the computer.
'''
letters = ['a', 'b', 'c', 'd', 
'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p',
 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 
'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '8', '9']

symbols = ['!', '#', '$', '%', '&', '^', '(', ')', '', 
'*', '+']

print("welcome to password Generator")
nr_letters = int(input("How many letters would you like i your password?\n"))
nr_symbols = int(input("How many symbols would you like i your password?\n"))
nr_numbers = int(input("How many numbers would you like i your password?\n"))

# there two ways to do this, easy and hard way 

# SOLUTION

# password = ""
# for char in range(1, nr_letters + 1):
#     #  random_char = random.choice(letters)
#     #  print(random_char) 
#     #  password += random_char
#     #  print(password)
#     # or we can short it by using
#     password += random.choice(letters)


# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)

# print(password)


'''
the problem here is that its easy for a hacker to guess your password.
knowing fully that there is always 4digits in same place, in order to tackle that we 
are going to be using the hard level
'''

# SOLUTION to HARD LEVEL

password_list = []  #list

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters)) #appending the letters

 
for  char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

# now lets turn it back to a string
password = ""
for char in password_list:
    password += char

print(f"Your password is {password}")

"""
create a program that would put everything together....
"""

# conf_pass = input("Confirm password!")

# if password == conf_pass:
#     print("Successfully logged in")

# else:
#     print("invalid password\n")
