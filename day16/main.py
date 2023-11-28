from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    order = input(f"what would you like {menu.get_items()}?: ")
    if order == "report":
        coffe_maker.report()
    else:
        order_object = menu.find_drink(order)
        if coffe_maker.is_resource_sufficient(order_object) and money_machine.make_payment(order_object.cost):
            coffe_maker.make_coffee(order_object)

