from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# no code here before now.
'''{Program requirements are:}
{Step one: Print report}
'''
# creating a report through the money_machie & cofee_maker
money_machine = MoneyMachine()
cofee_maker = CoffeeMaker()

# creating a report through the money_machine & cofee_maker
# money_machine.report()
# cofee_maker.report()

'''
{Step two: check resources sufficient}

'''
menu = Menu()
 
is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off": 
        print("GoodBye") 
        is_on = False
    elif choice == "report":
        cofee_maker.report()
        money_machine.report() 
    else:
        drink = menu.find_drink(choice)
        # print(drink)
        '''checking if the resources required are complete'''
        # print(cofee_maker.is_resource_sufficient(drink))
        # if cofee_maker.is_resource_sufficient(drink):
        #     '''{Step three: process coins and step step four, check transaction succeeful}'''
        #     # print(money_machine.make_payment(drink.cost))
        #     if cofee_maker.is_resource_sufficient(drink):
        #         '''{step five: Make coffee}'''
        #         cofee_maker.make_coffee(drink)
                
        '''{Simplified code}'''
        
        if cofee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
             cofee_maker.make_coffee(drink)
        