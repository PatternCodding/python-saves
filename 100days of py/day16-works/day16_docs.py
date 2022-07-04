'''
late steve Jobs: this man explained OOP in the best format for a better understanding. 
he nareted a story of you travelling to japan, when you get there you find out that your clothe
is stained by some stuffs, where as you don't really know where you're, you don't speak japan,
neither do you use there currency or any means of communication.

{SOLUTION}: going to the hotel attendance who surely knows how to speak English and defnatetly
can make use of your currency, explainiing everting to them, surely your problems are solved.

{OOP to build a coffee machine with same program requirements}
essentially easy to work with while using OOP, importing and using different kind of modules




MenuItem Class

Attributes:

        

        name
        (str) The name of the drink.

        e.g. “latte”


        cost
        (float) The price of the drink.

        e.g 1.5


        ingredients
        (dictionary) The ingredients and amounts required to make the drink.

        e.g. {“water”: 100, “coffee”: 16}



Menu Class

Methods:


        get_items()
        Returns all the names of the available menu items as a concatenated string.

        e.g. “latte/espresso/cappuccino”


        find_drink(order_name)
        Parameter order_name: (str) The name of the drinks order.

        Searches the menu for a particular drink by name. Returns a MenuItem object if it exists, otherwise returns None.



CoffeeMaker Class

Methods:


        report()
        Prints a report of all resources.

        e.g.

        Water: 300ml

        Milk: 200ml

        Coffee: 100g


        is_resource_sufficient(drink)
        Parameter drink: (MenuItem) The MenuItem object to make.
        Returns True when the drink order can be made, False if ingredients are insufficient.

        e.g.
        True


        make_coffee(order)
        Parameter order: (MenuItem) The MenuItem object to make.

        Deducts the required ingredients from the resources.



MoneyMachine Class

Methods:

        report()
        Prints the current profit

        e.g.

        Money: $0


        make_payment(cost)
        Parameter cost: (float) The cost of the drink.

        Returns True when payment is accepted, or False if insufficient.

        e.g. False



'''
