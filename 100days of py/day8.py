# functions and inputs
'''
create a fuction called great and tell it to do three thing
'''

# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("isn't the wheater nice today?")

# greet()
# lets try greeting a particular person, ie adding a paramters


# function that allows for an input
# def greet_with_name(name): #parameter = the name of the ....
#     print(f"Hello {name}")
#     print(f"How do you do {name}")
 
# greet_with_name("Chinedum") #argument = actual value


# functions with multiple inputs
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"what is it like in {location}")  # positional arguments

# greet_with("Patterson", "Lagos state")
# trying to interchage the result or the arguments

# the solution is by using what is called [keyword arguments]
# greet_with(location="Lagos state", name="Patterson")


# Excercise:
'''
creating a program that would calculate how many paints that is required to paint a particular house
 instruction: the paint can says that 1 can of paint can cover over 5 square meters of wall, Given a random
 height and width of wall.
 calculate how many cans of paints you will need to buy

 number of cans = (wall height x wall width) / avearge per can

 e.g. Height = 2, width = 4, Coverage = 5

 number of can = (2 x 4) / 5 = 1.6

 But bcos you cant buy 0.6 of a can paint, the result should be rounded up to 2 cans.
'''
# SOLUTION
# import math
# def paint_calc(height, width, cover):
#     area = height * width
#     num_of_cans = math.ceil(area / cover)
#     print(f"You'll need {num_of_cans} cans of paints. ")

# test_h = int(input("Height of a wall:  "))
# test_w = int(input("Weight of a wall:  "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)


# lets create a prime number checker
# what are prime numbers?
# numbers that can be broken smaller parts other than 1 and its self

# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i ==0:
#             is_prime = False
#         if is_prime:
#             print("It's a prime number. ")
#         else:
#             print("It's not a prime number. ")

# n = int(input("Check this Number:  "))
# prime_checker(number=n)


# we are going to build a caecer cipher


'''
STEPS: 1) create a function called 'encrpt', that takes the 'text' and 'ahift' as inputs.
2) inside the 'encrypt' function shift each letter of the 'text' farwards in the alphabet
by the shift alphabet by the shift amount and print the encrypted text.

e.g
plain_text = "hello"
shift = 5
cipher_text = "mjqqt"
print output: the entered text is mjqqt

3) call the encrypt funtion and pass in the user inputs. You should be able to test the code encrypt as message

decypt function:
1) create a funtion called 'decrypt' that takes the 'text' and 'shift' as inputs.
2) inside the 'decrypt' function, shift each letter of the 'text' *backward* in the alphabet in the shift amount and print the decrypt tet.

e.g
cipger_text = 'mjqqt'
shift = 5
plain_text = "hello"
print output: the decoded text is hello

check if the user wanted to encrypt or decrypt the message by checking 'direction' variable. then call the correct function based
on the direction varaiable. You should be able to test the code to encypt a message.
'''

alphabet = ['a', 'b', 'c', 'd', 
'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p',
 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
 'a', 'b', 'c', 'd',  #not yet to add
'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p',
 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
 ]


# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_postion = position + shift_amount
#         new_letter = alphabet[new_postion]
#         cipher_text += new_letter
# now what happends when we want to encode a letter that is closer to the end of the alphabets something like zulu?
# now to solve this, we need to copy the alphabets and duplicate it once more


    # print(f"The encode text is {cipher_text}")

# # now lets decrypt
# def decrypt(cipher_text, shift_amout):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amout
#         plain_text += alphabet[new_position]
#     print(f"the decode text is {plain_text}")

# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amout=shift)


'''
since both the encrypt and decrypt functions are almost thesame thing why not combine them together!
with a function called ceasar(), and get rid of the if and elif statement

call the ceasar() function, passing over the 'text', 'shift' and 'direction' values
'''

def ceasar(start_text, shift_amount, ciphar_direction):
    end_text = ""
    if ciphar_direction == "decode":
        shift_amount *= -1 # or shift_amount = shift_amount * -1
    for char in start_text: #change the letter to char
        # allowing spaces and symbols
        if char in alphabet:
            position = alphabet.index(char)
        # once the if satatement is found inside the for loop, there will be an error, therefore we should put it before it.
        # if ciphar_direction == "decode":
        #     shift_amount *= -1 # or shift_amount = shift_amount * -1
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            # append the text
            end_text += char
    print(f"Here's the {ciphar_direction}d result:   {end_text}")

 
#  what of if user enters a shift that is geater than number of letters in the alphabet?
# this can be done using modulus (%)


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) 



    # allowing spaces and syboles.
    # and also runnuing it again and again while the user type yes

    # the solution is found after the for loop

    shift = shift % 26
    ceasar(start_text=text, shift_amount=shift, ciphar_direction=direction)

    result = input("Type 'yes' to continue others 'no' to quite.\n")
    if result == "no":
        should_continue = False
        print("Goodbye!")