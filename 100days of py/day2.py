# primitive values
# just as we just finished learning how to get the
# lenght of a string, how then will we be able to get that of numbers?


#BASIC DATA TYPES IN PYTHON
# '''
# 1. String
# 2. integer
# 3. float
# 4. Boolean
# 5. 
# '''

# # string: this are combinations of characters
# # methods in character
# # 1. subscriptin: the process of pulling out a particular character 
# among others

# names = ("Chinedum Patterson"[0])
# names = ("Chinedum Patterson"[0:12])
# names = ("Chinedum Patterson"[-1])
# print(names)


# # 2. Integers: this are values without a decimal places with or without 
# a negative values
# num1 = 12
# num2 = 10

# print("this are numbers",num1 + num2)


# # string numbers
# strNum1 = "123"
# strNum2 = "456"

# print("this numbers",strNum1 + strNum2)

# # Floating values: numbers with decimal places

# float1 = 123.23
# float2 = 23.123

# print("this are floating values",float1 * float2)

# this is called type conversion in python
# trying to get lenght of an input that has numbers
# num_char = len(input("enter your names "))
# new_num_char = str(num_char)
# print("your name has " + new_num_char +  " characters.")


# excercise conver numbers to inter and float 

# calc1 = int(input("Enter first number to calculate\n"))
# calc2 = int(input("Enter second number to calculate\n"))
# calc3 = calc1 + calc2
# print("the addtion of both is >\n",calc3)



# arithmetic operators in python
# 3 + 4
# 3 - 4
# 3 * 4
# 3 / 4
# 3 ** 4  #power
   
# operator precedence

# PEMDAS: [1.(), 2.**, 3.*, 4./, 5.+, 6.-]. ie parenthesis, power, multiplication, division,add,sub.
# print(3 * 3 + 3 / 3 -3 )
# print(3 * (3 + 3) / 3 -3 )
# print(18/3-3)

# Assignment:write a program that will calculate the body mass index (MBI) of a user input
# formular for BMI
# the result should be in a whole number form
# this is used to measure to somebodys 
# BMI = weight(kg)/height^2(m^2)

# solution

# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# BMI = weight / height ** 2
# print("your your BMI is:")
# print(int(BMI))

# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# BMI = int(weight) / float(height)  ** 2
# print("your your BMI is:")
# print(int(BMI))

# Number manipulations

# print(8/3)
# print(int(8/3)) #integer conversion, chop up the remainig values...
# print(round(8/3)) #rounding number upward depending on the decimal value that follows immidiatly
# print(round(8/3, 2)) #rounding number upward according to your decision
# print(int(8//3)) #this as well chop off the remaiders

# score = 0
# # adding values to the score
# score +=2
# print(score)


# FORMATTING STRING

# score = 100
# height = 1.8
# isWinning = True
# print(f"your score is {score} and your height is {height} and your winning is {isWinning}")

# Assignment:
# write a program that would tell a user how many days, weeks and
# and months he/she is lucky enough to live till 100yrs old

# Tips: 
# there are 365 days in a year
# 52 weeks in a year
# 12 months in year

# solution
# current = int(input("Enter your current year\n"))
# years_remaining = 100 - current
# days_remainig = years_remaining * 365
# weeks_remaining = years_remaining * 52
# months_remaning = years_remaining * 12

# print(years_remaining)
# print(days_remainig)
# print(weeks_remaining)
# print(months_remaning)

# using formatting string
# print(f"you have {years_remaining} yeas, {months_remaning} months, {weeks_remaining} weeks and {days_remainig} days left for you to die!")

# print(f""""
#       "you have {years_remaining} years remaining,
#        {months_remaning} months,
#        {weeks_remaining} weeks and
#        {days_remainig} days left for you to be 100 years if you have Jesus Christ in your life!

# """)

# Assignment three
# create a calculator that would say:
# 1. Welcome to my calculator
# 2. what was the total bill in $
# 3. what percentage would you like to pay from the bill
# 4. how many people are going to share with you on paying the bill bill?
# 5. each person should pay so so amount in $
# make the bill to have at least two to three decimal numbers

# how to calculate a percentage is by multiplying the number by the percentage of the number divided by 100
# if the bill is $150.00, split between 5 people, with $12, tip,
# let say 12 / 100 = 0.12
# then multiply total amount by it, such as $150 * 0.12 = 18.0
# then we add the tip onto the final bill = 150 + 18 = $168
# short hand of doing this is: 150 * 1.12 = same answer.
# next step is to divide it by the people, wich is 158 / 5 = 33.6
# each person should pay ()


# Solution

# print("Welcome to my tip calculator! ")
# bill = float(input("what was the total bill? $ "))
# tip = float(input("what percentage would you like to give 10, 12 15 ? $"))
# people = int(input("How many people are going to pay it? $"))


# tip_percent = tip / 100
# total_tip_amount = bill * tip_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# # final_amount = round(bill_per_person, 2)
# final_amount = "{:.2f}".format(bill_per_person)
# print(f"each person should pay: ${final_amount}")


# well this project is actuall not 100% correct. what of if we decide to enter $150
# with percetage of $12, and people to be 5. you'll notice that there's no two decimal places
# solution to that, using what's called
# final_amount = "{:.2f}".format(bill_per_person)


# bill_with_tip = tip / 100 * bill + bill
# bill_per_person = bill_with_tip / people
# final_amount = round(bill_per_person, 2)
# print(f"each person should pay: ${final_amount}")
# # to have two decimal places
# final_amount = "{:.2f}".format(bill_per_person)
# print(f"each person should pay: ${final_amount}")

