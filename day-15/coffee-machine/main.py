"""Coffee machine sim"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


MONEY = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def process_coins():
    """Counts up the amount of each type of coin inserted and returns a decimal value"""
    total = int(input("How many Quarters?: ")) * 0.25
    total += int(input("How many Dimes?: ")) * 0.1
    total += int(input("How many Nickles?: ")) * 0.05
    total += int(input("How many Pennies?: ")) * 0.01
    return total


def resources_sufficient(drink_ingredients):
    """Checks if there are enough ingredients to make the selected drink"""
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def transaction_successful(amount_paid, drink_name):
    """Returns True is amount paid is equal to or more than cost of drink"""
    global MONEY
    if amount_paid > drink_name['cost']:
        change = round(amount_paid - drink_name['cost'], 2)
        MONEY += amount_paid
        print(f"Here is ${change} in change.")
    elif amount_paid == drink_name['cost']:
        MONEY += amount_paid
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    return True


def make_coffee(drink_name, drink_ingredients):
    """Removes ingredients from the coffee machine storage"""
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


IS_ON = True

while IS_ON:
    choice = input("What would you like? (espresso/latte/cappuccino) ")
    if choice == "off":
        IS_ON = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${round(MONEY, 2)}")
    else:
        drink = MENU[choice]
        if resources_sufficient(drink['ingredients']):
            payment = process_coins()
            if transaction_successful(payment, drink):
                make_coffee(choice, drink['ingredients'])
