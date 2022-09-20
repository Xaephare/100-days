from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

IS_ON = True
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


while IS_ON:
    menu_options = menu.get_items()
    choice = input(f"What would you like? ({menu_options})")
    if choice == "off":
        IS_ON = False
    elif choice == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)
