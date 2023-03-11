from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

c = CoffeeMaker()
m = MoneyMachine()
men = Menu()
is_on = True
while is_on:
    user_choice = input(f"What would you like? {men.get_items()}:").lower()
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        c.report()
        m.report()
    else:
        retval = men.find_drink(user_choice)
        if c.is_resource_sufficient(retval):
            if m.make_payment(retval.cost):
                c.make_coffee(retval)
