MENU = {
    "espresso": {
        "ingredients": {
            "milk": 0,
            "water": 50,
            "coffee": 18,
        },
        "cost": 250,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 200,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 175,
    }
}

resources = {
    "water": 1000,
    "milk": 1000,
    "coffee": 250,
}


cost = 0
total_money = 0
counter = 0


def report():
    # # Method 1... can be used only for this code
    # print(f"water : {resources['water']} ml")
    # print(f"milk : {resources['milk']} ml")
    # print(f"Coffee : {resources['coffee']} g")
    # print(f"Total collection : ${total_money}")
    # print(f"Total orders delivered : {counter}")
    # print("\n")

    # Method 2... More generalized ... in case you add more ingredients to the resources
    for item in resources:
        print(f"{item} : {resources[item]}")
    print(f"Total collection : ${total_money}")
    print(f"Total orders delivered : {counter}")
    print("\n")


def check_resources():
    # #Method 1 for check resources.... does not specify exactly which resource is insuffficient
    #     if resources['water'] >= MENU [choice]["ingredients"]["water"] and resources['milk'] >= MENU [choice]["ingredients"]['milk'] and resources['coffee'] >= MENU[choice]["ingredients"]["coffee"]:
    #         return True
    #     else:
    #         print("Insufficient resources. Sorry for the inconvenience")
    #         return False

    # Method 2.... better as it gives exactly which resource is insufficient
    for item in resources:
        if MENU[choice]['ingredients'][item] > resources[item]:
            print(f"insufficient {item}")
            print("Sorry for inconvenience, the order cannot be executed due to insufficient resources.")
            return False
    return True


def money_check():
    global cost, total_money

    usr_two_hundred = int(input("How many $200: "))
    usr_hundred = int(input("How many $100: "))
    usr_fifty = int(input("How many $50: "))
    usr_twenty = int(input("How many $20: "))
    usr_ten = int(input("How many $10: "))
    usr_five = int(input("How many $5: "))

    cost = (200 * usr_two_hundred) + (100 * usr_hundred) + (50 * usr_fifty) + (20 * usr_twenty) + (10 * usr_ten) + (5 * usr_five )
    # print(cost)

    if cost == MENU[choice]['cost']:
        total_money += MENU[choice]['cost']
        return True
    elif cost >= MENU[choice]['cost']:
        total_money += MENU[choice]['cost']
        change = cost - MENU[choice]['cost']
        print(f"Here is your change : ${change}")
        return True
    else:
        print("\nSorry that's not enough money. Money Refunded\n")
        return False


def make_coffee():
    global resources
    ## Method 1
    # resources['water'] -= MENU [choice]["ingredients"]["water"]
    # resources['milk'] -= MENU [choice]["ingredients"]["milk"]
    # resources['coffee'] -= MENU [choice]["ingredients"]["coffee"]

    ##Method 2
    for item in resources:
        resources[item] -= MENU[choice]["ingredients"][item]
    print(f"\nHere's your {choice}. Enjoy!!! \n")


def coffee_cost():
    for item in MENU:
        print(f"{item} : ${MENU [item]['cost']}")



should_continue = True
while should_continue:
    coffee_cost()
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == 'off':
        should_continue = False

    elif choice == 'report':
        print("Here's the report so far")
        report()

    elif choice == 'latte' or choice == 'cappuccino' or choice == 'espresso':
        if check_resources():
            if money_check():
                counter += 1
                make_coffee()

        repeat = input("Would you like to place another order? Type 'Y' for Yes and 'N' for No : ").lower()
        if repeat == 'y':
            should_continue = True
        elif repeat == 'n':
            should_continue = False
        elif repeat == "off":
            should_continue = False
        elif repeat == 'report':
            report()
            should_continue = True
        else:
            print("Invalid input. Please enter a valid input")
    else:
        print("Invalid input. Please enter a valid input")

