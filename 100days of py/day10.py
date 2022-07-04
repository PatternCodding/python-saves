# More about a function and ones with inputs
# the flavour of function
 


# function with Output

# def  format_name(f_name, l_name): #havng a title name
#     print(f_name.title())
#     print(l_name.title())
    
# format_name("Chinedum", "PATTERSON")
    

# introducing return function
# def  format_name(f_name, l_name): #havng a title name
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     print(f"{formated_f_name} {formated_l_name}")
    
# format_name("ChInEdUm", "PATTERSON")
    
def  format_name(f_name, l_name): #havng a title name
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return(f"{formated_f_name} {formated_l_name}")
# note anything after the return fuction will be ignored, and wont be print out

    
# format_string = format_name("ChInEdUm", "PATTERSON")
# print(format_string)

# OR
# print(format_name("chinedum", "Patterson"))


# def  format_name(f_name, l_name): #havng a title name
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return(f"{formated_f_name} {formated_l_name}")
# print(format_name(input("whats your First Name? "), 
#         input("Whats your last name? ")))


# returning an empty string


# excercie , fix this bug 


def  format_name(f_name, l_name): 
    if f_name  or l_name == "":
        return "You didn't provide valid inputs"
    elif f_name  or l_name != "":        
        formated_f_name = f_name.title()
        formated_l_name = l_name.title()
#         return(f"{formated_f_name} {formated_l_name}")
# print(format_name(input("whats your First Name? "), 
#         input("Whats your last name? ")))

# # solution
# def  format_name(f_name, l_name): 
#     if f_name  or l_name != "":        
#         formated_f_name = f_name.title()
#         formated_l_name = l_name.title()
#         return(f"{formated_f_name} {formated_l_name}")
#     elif f_name  or l_name == "":
#         return "You didn't provide valid inputs"
# print(format_name(input("whats your First Name? "), 
#         input("Whats your last name? ")))


# using return statement to know which is a leep year

# def  is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False 
#         else:
#             return True
#     else:
#         return False  
        
        
# def  days_in_month(year, month):
#     if month > 12 or month < 1:
#         return "Invalid month"
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year) and month == 2:
#         return 29
#     return month_days[month - 1]
    
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)
    
    
# Docstrings in python: this are basically a way for us to create litle bits of documentation as we're coding 
# along in our functions or in our other blocks of code 

# built in function like len(retuns number of data), lets create our own using docstring

# this allows us to write multiple lines of code iusing three """" docsrings goes here """"



# calculator project

def  add(n1, n2):
    return n1 + n2    

def  sub(n1, n2):
    return n1 - n2    

def  mul(n1, n2):
    return n1 * n2    

def  div(n1, n2):
    return n1 / n2    

# using a dictionary to store dictionaries for the keys and values

operations = {
    "+": add,
    "": add,
    "*": add,
    "/": add
}
num1 = int(input("Enter first number "))

for symbol in operations:
    print(symbol) 
operator_symbol = input("pick an operator from the line above: ")
num2 = int(input("Enter second number "))
calculation_fuction = operations[operator_symbol]
answer = calculation_fuction(num1, num2)


print(f"{num1} {operator_symbol } {num2} = {answer}")


# printing vs returning function
# actually return fuc. helps us to reuse a value often and often

operator_symbol = input("pick up another operator from the line above: ")
num3 = int(input("Enter next number "))
calculation_fuction = operations[operator_symbol]
second_answer = calculation_fuction(calculation_fuction(num1, num2), num3) #i called the function twice bcos am using return statement



print(f"{answer} {operator_symbol } {num3} = {second_answer}")