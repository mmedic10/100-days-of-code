from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
#menu_items = MenuItem()
coffe_machine = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True



while is_on==True:
    option = menu.get_items()
    answer = input(f"What's would you like? ({option})")
    if answer == "off":
        is_on = False
    elif answer == "report":
        print(coffe_machine.report())
        print(money_machine.report())
    else:
        drink = menu.find_drink(answer)
        if coffe_machine.is_resource_sufficient(drink) == True:
            payment = money_machine.make_payment(drink.cost)
            if payment == True:
                coffe_machine.make_coffee(drink)