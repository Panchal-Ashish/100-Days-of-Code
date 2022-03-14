from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
# import coffee_maker
from money_machine import MoneyMachine
# import money_machine


money_machine = MoneyMachine()
# my_money_machine = money_machine.MoneyMachine()


coffee_maker = CoffeeMaker()
# coffee_maker = coffee_maker.CoffeeMaker()

menu = Menu()


is_on = True
while is_on:
    options = menu.get_items()
    print("\n")
    menu.menucard()
    choice = input(f"What would you like? ({options}): ").lower()
    if choice == "off":
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice in options:
        drink = menu.find_drink(choice)    # catches hold of all elements (ingredients + cost) of the drink
        print(f"cost of {drink.name} is ${drink.cost}")
        is_resource_sufficient = coffee_maker.is_resource_sufficient(drink)
  
        if is_resource_sufficient == True:
            if money_machine.make_payment(drink.cost) == True:
                coffee_maker.make_coffee(drink)

                print("\n")
                repeat = input("Would you like to place another order? Type 'Y' for yes and 'N' for No: ").lower()

                if  repeat == 'y':
                    is_on = True
                elif repeat == 'n':
                    is_on = False
                elif repeat == 'report':
                    coffee_maker.report()
                    money_machine.report()
                elif repeat == 'off':
                    is_on = False
                else:
                    print("Invalid input. Please give a valid input")
        else:
            coffee_maker.report()
            money_machine.report()
            is_on = False

    else:
        print("Invalid input. Please give a valid input")
